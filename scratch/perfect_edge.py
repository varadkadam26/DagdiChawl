import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Manish\.gemini\antigravity-ide\brain\8b48d514-085d-423f-9f74-6affb060217e\.user_uploaded\media_1791709581788.jpg')
idol = cv2.imread('public/images/devi_hd_clean.png', cv2.IMREAD_UNCHANGED)
a = idol[:, :, 3]
k = np.ones((3, 3), np.uint8)

for i in [1, 2, 3]:
    a_er = cv2.erode(a, k, iterations=i)
    edge = (cv2.dilate((a_er == 0).astype(np.uint8), k) > 0) & (a_er == 255)
    edge_rgb = idol[edge, :3]
    pct = np.mean(np.mean(edge_rgb, axis=1) > 200) * 100
    print(f"Iter {i}: Edge pixels: {np.sum(edge)}, Mean: {np.mean(edge_rgb):.1f}, >200 pct: {pct:.1f}%")
