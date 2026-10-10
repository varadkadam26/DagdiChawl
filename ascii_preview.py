from PIL import Image
import glob
import sys

def image_to_ascii(image_path, width=40):
    try:
        img = Image.open(image_path)
        img = img.resize((width, int((width/img.width) * img.height * 0.55)))
        img = img.convert('L')
        
        pixels = img.getdata()
        chars = ["B","S","#","&","@","$","%","*","!",":","."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        
        pixel_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + width] for index in range(0, pixel_count, width)]
        
        print(f"\n--- {image_path} ---")
        print("\n".join(ascii_image))
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

for f in sorted(glob.glob('public/images/marquee/new_*.*')):
    if not ('6' in f or '7' in f or '8' in f or '9' in f or '10' in f):
        image_to_ascii(f)
