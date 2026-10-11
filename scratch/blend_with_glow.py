import cv2
import numpy as np

# Load clean cave background
cave = cv2.imread('scratch/clean_hero_mobile.jpg')
idol = cv2.imread('public/images/devi_hd_clean.png', cv2.IMREAD_UNCHANGED)

idol_w = 750
idol_h = 932
idol_x = 146
idol_y = 474

resized_idol = cv2.resize(idol, (idol_w, idol_h), interpolation=cv2.INTER_LANCZOS4)
alpha_idol = (resized_idol[:, :, 3].astype(np.float32) / 255.0)[:, :, np.newaxis]
rgb_idol = resized_idol[:, :, :3].astype(np.float32)

# Create a divine golden aura mask behind the idol
# 1. Broad soft ambient gold glow (sigma = 45)
glow_mask_large = cv2.GaussianBlur(resized_idol[:, :, 3].astype(np.float32), (101, 101), 35.0) / 255.0
# 2. Intense inner golden rim glow (sigma = 15)
glow_mask_rim = cv2.GaussianBlur(resized_idol[:, :, 3].astype(np.float32), (51, 51), 12.0) / 255.0

# Extract ROI from cave
roi = cave[idol_y:idol_y+idol_h, idol_x:idol_x+idol_w].astype(np.float32)

# Golden colors (BGR format):
# Deep warm gold: [B=20, G=150, R=255]
# Bright divine gold: [B=50, G=215, R=255]
gold_deep = np.zeros_like(roi)
gold_deep[:, :] = [15, 140, 245]

gold_bright = np.zeros_like(roi)
gold_bright[:, :] = [45, 205, 255]

# Blend glowing aura onto the cave ROI (additive screen blend)
# Broad aura:
aura_layer = gold_deep * glow_mask_large[:, :, np.newaxis] * 0.75 + gold_bright * glow_mask_rim[:, :, np.newaxis] * 0.65

# Composite aura onto cave background using soft screen/add blend
roi_with_glow = roi + aura_layer * (1.0 - roi / 255.0)
roi_with_glow = np.clip(roi_with_glow, 0, 255)

# Now composite Devi Maa on top with her perfectly finished feathered edge:
final_roi = rgb_idol * alpha_idol + roi_with_glow * (1.0 - alpha_idol)
final_roi = np.clip(final_roi, 0, 255)

# Place into cave
final_hero = cave.copy()
final_hero[idol_y:idol_y+idol_h, idol_x:idol_x+idol_w] = final_roi.astype(np.uint8)

# Save hero_mobile.jpg with 100% quality and 4:4:4 sampling
cv2.imwrite('public/images/hero_mobile.jpg', final_hero, [
    cv2.IMWRITE_JPEG_QUALITY, 100,
    cv2.IMWRITE_JPEG_SAMPLING_FACTOR, cv2.IMWRITE_JPEG_SAMPLING_FACTOR_444
])
print("Successfully generated and saved public/images/hero_mobile.jpg with clean edges and golden aura!")

# Save resized clean transparent idol for direct use
cv2.imwrite('public/images/devi_mobile_hd.png', resized_idol)
print("Saved public/images/devi_mobile_hd.png")
