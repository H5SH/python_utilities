from PIL import Image
import os
from pillow_heif import register_heif_opener

def convert_heic_to_png(heic_path, png_path):
    register_heif_opener()
    try:
        with Image.open(heic_path) as heic_img:
            heic_img.convert('RGB').save(png_path, formate='PNG')
    except Exception as e:
        print(e)

heic_directory = "new"

png_directory = "new_images"

img_path = "new"

for file in os.listdir(img_path):
    if file.endswith('.HEIC') or file.endswith(('.heic', 'jpg', 'jpeg')):
        heic_path = os.path.join(heic_directory, file)
        png_path = os.path.join(png_directory, os.path.splitext(file)[0] + ".png")
        convert_heic_to_png(heic_path, png_path) 


