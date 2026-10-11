import cv2
import numpy as np

# Create standard 1200x630 Open Graph preview image
w, h = 1200, 630
og = np.zeros((h, w, 3), dtype=np.uint8)

# Load cave background if available or create rich gradient
cave = cv2.imread('scratch/clean_hero_mobile.jpg')
if cave is not None:
    # Resize and center crop cave to 1200x630
    ch, cw = cave.shape[:2]
    # Crop top 60% of cave
    crop_cave = cave[int(ch * 0.1):int(ch * 0.8), :]
    og = cv2.resize(crop_cave, (w, h), interpolation=cv2.INTER_LANCZOS4)
    # Darken sides slightly for dramatic focus on Devi Maa
    vignette = np.zeros((h, w), dtype=np.float32)
    cv2.circle(vignette, (w // 2, h // 2), int(w * 0.6), 1.0, -1)
    vignette = cv2.GaussianBlur(vignette, (151, 151), 75.0)
    og = (og * (0.4 + 0.6 * vignette[:, :, np.newaxis])).astype(np.uint8)
else:
    # Rich dark maroon/gold gradient
    for y in range(h):
        factor = y / float(h)
        og[y, :] = [int(5 + 10 * factor), int(4 + 15 * factor), int(15 + 35 * factor)]

# Load clean Devi idol
idol = cv2.imread('public/images/devi_hd_clean.png', cv2.IMREAD_UNCHANGED)
if idol is not None:
    # Scale idol to fit nicely in the height (height ~ 580px)
    idol_target_h = 580
    idol_target_w = int(idol.shape[1] * (idol_target_h / float(idol.shape[0])))
    resized_idol = cv2.resize(idol, (idol_target_w, idol_target_h), interpolation=cv2.INTER_LANCZOS4)
    
    # Position in center
    pos_x = (w - idol_target_w) // 2
    pos_y = h - idol_target_h - 10
    
    # Golden glow behind idol
    alpha = (resized_idol[:, :, 3].astype(np.float32) / 255.0)
    glow_large = cv2.GaussianBlur(alpha, (81, 81), 28.0)
    
    roi = og[pos_y:pos_y+idol_target_h, pos_x:pos_x+idol_target_w].astype(np.float32)
    gold = np.zeros_like(roi)
    gold[:, :] = [30, 190, 255] # BGR gold
    
    # Screen blend aura
    roi = roi + gold * glow_large[:, :, np.newaxis] * 0.75 * (1.0 - roi / 255.0)
    
    # Blend idol on top
    rgb = resized_idol[:, :, :3].astype(np.float32)
    a_3d = alpha[:, :, np.newaxis]
    blended = rgb * a_3d + roi * (1.0 - a_3d)
    
    og[pos_y:pos_y+idol_target_h, pos_x:pos_x+idol_target_w] = np.clip(blended, 0, 255).astype(np.uint8)

cv2.imwrite('public/images/og_share.jpg', og, [cv2.IMWRITE_JPEG_QUALITY, 96])
print("Successfully generated public/images/og_share.jpg (1200x630)!")
