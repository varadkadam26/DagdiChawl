import cv2
import numpy as np

# 1. Load clean cave background
cave = cv2.imread('scratch/clean_hero_mobile.jpg')
idol = cv2.imread('public/images/devi_hd_clean.png', cv2.IMREAD_UNCHANGED)

idol_w = 750
idol_h = 932
idol_x = 146
idol_y = 474

resized_idol = cv2.resize(idol, (idol_w, idol_h), interpolation=cv2.INTER_LANCZOS4)
alpha_idol = (resized_idol[:, :, 3].astype(np.float32) / 255.0)[:, :, np.newaxis]
rgb_idol = resized_idol[:, :, :3].astype(np.float32)

# Extract ROI from cave
roi = cave[idol_y:idol_y+idol_h, idol_x:idol_x+idol_w].astype(np.float32)

# Subtle, pure warm ROYAL GOLD aura (STRICTLY NO YELLOW):
# Royal Gold in BGR: [B=45, G=165, R=210] (#D2A52D)
# Warm Amber Gold in BGR: [B=20, G=130, R=180] (#B48214)
glow_mask_broad = cv2.GaussianBlur(resized_idol[:, :, 3].astype(np.float32), (81, 81), 25.0) / 255.0
glow_mask_rim = cv2.GaussianBlur(resized_idol[:, :, 3].astype(np.float32), (41, 41), 10.0) / 255.0

gold_broad = np.zeros_like(roi)
gold_broad[:, :] = [20, 130, 180]  # BGR

gold_rim = np.zeros_like(roi)
gold_rim[:, :] = [45, 165, 210]  # BGR

# Subtle aura intensity: 0.35 broad, 0.30 rim
aura_layer = gold_broad * glow_mask_broad[:, :, np.newaxis] * 0.35 + gold_rim * glow_mask_rim[:, :, np.newaxis] * 0.30

# Blend aura strictly onto cave background
roi_with_glow = roi + aura_layer * (1.0 - roi / 255.0)
roi_with_glow = np.clip(roi_with_glow, 0, 255)

# Composite Devi Maa ON TOP of the glow:
# Where alpha_idol == 1 (inside Devi), it is 100% rgb_idol (Devi herself, zero glow on her)
final_roi = rgb_idol * alpha_idol + roi_with_glow * (1.0 - alpha_idol)
final_roi = np.clip(final_roi, 0, 255)

final_hero = cave.copy()
final_hero[idol_y:idol_y+idol_h, idol_x:idol_x+idol_w] = final_roi.astype(np.uint8)

# Save hero_mobile.jpg at max quality 100%
cv2.imwrite('public/images/hero_mobile.jpg', final_hero, [
    cv2.IMWRITE_JPEG_QUALITY, 100,
    cv2.IMWRITE_JPEG_SAMPLING_FACTOR, cv2.IMWRITE_JPEG_SAMPLING_FACTOR_444
])
print("Successfully generated public/images/hero_mobile.jpg with subtle royal gold aura strictly behind Devi!")
