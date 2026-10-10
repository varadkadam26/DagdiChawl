from PIL import Image

img = Image.open('public/images/final_page_no_text.jpg')
print('Size:', img.size)
w, h = img.size
pixels = img.convert('L').load()
bright_spots = []
for y in range(h):
    for x in range(w):
        if pixels[x,y] > 250:
            bright_spots.append((x,y))

print('Total bright pixels:', len(bright_spots))
if bright_spots:
    # cluster them roughly
    left_cluster = [p for p in bright_spots if p[0] < w//2]
    right_cluster = [p for p in bright_spots if p[0] >= w//2]
    if left_cluster:
        avg_lx = sum(p[0] for p in left_cluster) // len(left_cluster)
        avg_ly = sum(p[1] for p in left_cluster) // len(left_cluster)
        print(f"Left bright spot at: x={avg_lx}, y={avg_ly} ({avg_lx/w*100:.2f}%, {avg_ly/h*100:.2f}%)")
    if right_cluster:
        avg_rx = sum(p[0] for p in right_cluster) // len(right_cluster)
        avg_ry = sum(p[1] for p in right_cluster) // len(right_cluster)
        print(f"Right bright spot at: x={avg_rx}, y={avg_ry} ({avg_rx/w*100:.2f}%, {avg_ry/h*100:.2f}%)")
