import os
from PIL import Image
import shutil

def separate_images_by_dimensions(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        try: 
            with Image.open(file_path) as img:
                width, height = img.size
                dimension_folder_name = f"{width}x{height}"

                dimension_folder_path = os.path.join(output_directory, dimension_folder_name)
                os.makedirs(dimension_folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(dimension_folder_path, filename))
        except Exception as e:
            print(f"Error processing file {filename}: {e}")