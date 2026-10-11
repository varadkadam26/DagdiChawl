import cv2
import numpy as np

hero = cv2.imread('public/images/hero_mobile.jpg')
idol = cv2.imread('public/images/devi_hd_clean.png', cv2.IMREAD_UNCHANGED)

hero_gray = cv2.cvtColor(hero, cv2.COLOR_BGR2GRAY)
idol_bgr = idol[:, :, :3]
idol_alpha = idol[:, :, 3]

# Idol face / crown region for robust template matching
# Let's crop a high-contrast part of the idol, like the face & crown
# In idol (1024h x 824w):
# Crown & Face is roughly y: 150..350, x: 350..500
face_template = idol_bgr[150:350, 350:500]
face_gray = cv2.cvtColor(face_template, cv2.COLOR_BGR2GRAY)

best_val = -1
best_scale = 1.0
best_loc = (0, 0)

# Search scales around 0.8 to 1.3
for s in np.linspace(0.8, 1.3, 51):
    th = int(face_gray.shape[0] * s)
    tw = int(face_gray.shape[1] * s)
    resized_template = cv2.resize(face_gray, (tw, th))
    
    # Search in hero roughly y: 300..900, x: 200..900
    search_roi = hero_gray[300:1000, 200:900]
    res = cv2.matchTemplate(search_roi, resized_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if max_val > best_val:
        best_val = max_val
        best_scale = s
        best_loc = (max_loc[0] + 200, max_loc[1] + 300)

print(f"Best match val: {best_val:.4f} at scale: {best_scale:.4f}")
print(f"Face template top-left in hero: {best_loc}")

# Compute the top-left of the entire idol at best_scale:
# face template in idol was at (350, 150)
idol_w_scaled = int(round(idol.shape[1] * best_scale))
idol_h_scaled = int(round(idol.shape[0] * best_scale))

idol_x = int(round(best_loc[0] - 350 * best_scale))
idol_y = int(round(best_loc[1] - 150 * best_scale))

print(f"Idol scaled size: {idol_w_scaled} x {idol_h_scaled}")
print(f"Idol top-left in hero (1125x2000): x={idol_x}, y={idol_y}")

# Let's verify by overlaying and saving a test image
resized_idol = cv2.resize(idol, (idol_w_scaled, idol_h_scaled), interpolation=cv2.INTER_LANCZOS4)
alpha = (resized_idol[:, :, 3] / 255.0)[:, :, np.newaxis]
rgb = resized_idol[:, :, :3]

test_composite = hero.copy()
roi = test_composite[idol_y:idol_y+idol_h_scaled, idol_x:idol_x+idol_w_scaled]

# Alpha blend
blended = (rgb * alpha + roi * (1.0 - alpha)).astype(np.uint8)
test_composite[idol_y:idol_y+idol_h_scaled, idol_x:idol_x+idol_w_scaled] = blended

cv2.imwrite('scratch/test_overlay_aligned.jpg', test_composite)
print("Saved scratch/test_overlay_aligned.jpg")
