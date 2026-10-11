import cv2
import numpy as np

# 1. Load original image
orig = cv2.imread(r'C:\Users\Manish\.gemini\antigravity-ide\brain\8b48d514-085d-423f-9f74-6affb060217e\.user_uploaded\media_1791709581788.jpg')
h, w = orig.shape[:2]

# Checkerboard identification:
# Low saturation (diff between R, G, B <= 12) AND high brightness (val >= 200)
diff = np.max(orig, axis=2).astype(int) - np.min(orig, axis=2).astype(int)
val = np.mean(orig, axis=2)
is_cb = (diff <= 12) & (val >= 200)

# Connected components to identify the background connected to the image boundaries
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(is_cb.astype(np.uint8))
bg_mask = np.zeros((h, w), dtype=bool)

for i in range(1, num_labels):
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w_comp = stats[i, cv2.CC_STAT_WIDTH]
    h_comp = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    touches_border = (x == 0) or (y == 0) or (x + w_comp >= w) or (y + h_comp >= h)
    
    # Check if this component has the checkerboard pattern
    comp_vals = val[labels == i]
    has_cb = (np.min(comp_vals) < 235) and (np.max(comp_vals) > 248)
    
    if touches_border or (area > 200 and has_cb):
        bg_mask[labels == i] = True

# Add inner holes that are known background (e.g. between trishul and lion)
for i in range(1, num_labels):
    if not bg_mask[labels == i].any():
        cx, cy = centroids[i]
        area = stats[i, cv2.CC_STAT_AREA]
        if (570 <= cx <= 655) and (400 <= cy <= 860) and area > 80:
            bg_mask[labels == i] = True

# Create initial idol mask (255 where idol is, 0 where background is)
idol_mask = (~bg_mask).astype(np.uint8) * 255

# Fill any small accidental holes inside the idol
kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
idol_mask = cv2.morphologyEx(idol_mask, cv2.MORPH_CLOSE, kernel_close)

# 2. PROPER FINISHING ON OUTLINE / BORDER:
# Erode by 2 pixels to completely eliminate all white/gray checkerboard edge artifacts
kernel_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
clean_mask = cv2.erode(idol_mask, kernel_erode, iterations=2)

# Anti-alias and feather the boundary smoothly over 3 pixels:
# Distance transform inside and outside for a perfect continuous subpixel edge
dist_in = cv2.distanceTransform(clean_mask, cv2.DIST_L2, 5)
dist_out = cv2.distanceTransform(255 - clean_mask, cv2.DIST_L2, 5)

# Smooth transition from dist_in to dist_out around the boundary (-1.5px to +1.5px)
edge_range = 1.8
alpha = np.clip((dist_in - dist_out + edge_range) / (2.0 * edge_range), 0.0, 1.0)
alpha = cv2.GaussianBlur(alpha, (3, 3), 0.8)
alpha_uint8 = (alpha * 255).astype(np.uint8)

# 3. COLOR DE-FRINGING (despill) around the boundary:
# Where alpha is between 0.05 and 0.95, blend edge color with neighbor inside idol
edge_fringe = (alpha > 0.02) & (alpha < 0.98)
clean_rgb = orig.copy()

# Inpaint/diffuse colors from solid idol into the fringe region
inpaint_mask = ((alpha > 0) & (alpha < 0.85) & (val > 180) & (diff < 20)).astype(np.uint8)
clean_rgb = cv2.inpaint(clean_rgb, inpaint_mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Assemble 4-channel RGBA
rgba = np.dstack([clean_rgb, alpha_uint8])

# Save clean HD transparent idol
cv2.imwrite('public/images/devi_hd_clean.png', rgba)
cv2.imwrite('public/devi-idol.png', rgba)
print("Saved public/images/devi_hd_clean.png and public/devi-idol.png with smooth subpixel finished edges!")
