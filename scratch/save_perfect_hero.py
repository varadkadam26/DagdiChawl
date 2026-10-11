import cv2
import numpy as np

# Load original hero_mobile and the transparent clean idol
hero = cv2.imread('public/images/hero_mobile.jpg')
idol = cv2.imread('public/images/devi_hd_clean.png', cv2.IMREAD_UNCHANGED)

idol_w_scaled = 750
idol_h_scaled = 932
idol_x = 146
idol_y = 474

resized_idol = cv2.resize(idol, (idol_w_scaled, idol_h_scaled), interpolation=cv2.INTER_LANCZOS4)
alpha = (resized_idol[:, :, 3] / 255.0)[:, :, np.newaxis]
rgb = resized_idol[:, :, :3].astype(np.float32)

# Slight Gaussian feather on alpha edge (1px blur) for perfect antialiasing against the dark cave
alpha_feather = cv2.GaussianBlur(resized_idol[:, :, 3].astype(np.float32), (3, 3), 0) / 255.0
alpha_feather = alpha_feather[:, :, np.newaxis]

roi = hero[idol_y:idol_y+idol_h_scaled, idol_x:idol_x+idol_w_scaled].astype(np.float32)

# Blend
blended = rgb * alpha_feather + roi * (1.0 - alpha_feather)

final_hero = hero.copy()
final_hero[idol_y:idol_y+idol_h_scaled, idol_x:idol_x+idol_w_scaled] = np.clip(blended, 0, 255).astype(np.uint8)

# Save with maximum quality (100) and 4:4:4 chroma subsampling (no compression loss)
cv2.imwrite('public/images/hero_mobile.jpg', final_hero, [cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_JPEG_SAMPLING_FACTOR, cv2.IMWRITE_JPEG_SAMPLING_FACTOR_444])
print("Successfully generated and saved public/images/hero_mobile.jpg with 100% quality!")

# Also save transparent version in public/images for any direct asset use
cv2.imwrite('public/images/devi_mobile_hd.png', resized_idol)
print("Saved public/images/devi_mobile_hd.png")
