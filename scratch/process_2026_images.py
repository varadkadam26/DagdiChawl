import os
from PIL import Image

src_dir = r"C:\Users\Manish\.gemini\antigravity-ide\brain\8b48d514-085d-423f-9f74-6affb060217e\.user_uploaded"
files = [
    "media_1791717853346.png",
    "media_1791717864385.jpg",
    "media_1791717876679.jpg",
    "media_1791717884454.jpg"
]

target_dir = r"c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\public\images\glimpses"
os.makedirs(target_dir, exist_ok=True)

# Copy and convert if needed to 2026_new_1.jpg, 2026_new_2.jpg, 2026_new_3.jpg, 2026_new_4.jpg
for i, fname in enumerate(files, 1):
    src_path = os.path.join(src_dir, fname)
    im = Image.open(src_path)
    print(f"File {i}: {fname} -> size={im.size}, mode={im.mode}")
    if im.mode in ('RGBA', 'P'):
        rgb_im = im.convert('RGB')
    else:
        rgb_im = im
    dst_path = os.path.join(target_dir, f"2026_new_{i}.jpg")
    rgb_im.save(dst_path, "JPEG", quality=95, optimize=True)
    print(f"Saved: {dst_path} ({os.path.getsize(dst_path)} bytes)")
