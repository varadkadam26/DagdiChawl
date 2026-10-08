import rembg
from PIL import Image

# Use lighter model
session = rembg.new_session('u2net')

with open('input.jpg', 'rb') as i:
    with open('public/devi-idol.png', 'wb') as o:
        input_data = i.read()
        output_data = rembg.remove(input_data, session=session)
        o.write(output_data)
