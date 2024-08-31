import os
from PIL import Image
import imagehash
import shutil

def separate_similar_images(input_directory, output_directory, threshold = 100):

    os.makedirs(output_directory, exist_ok=True)

    image_hashes = {}
    group_files = []

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        try:
            with Image.open(file_path) as img:
                img_hash = imagehash.phash(img)

                found_group = False

                for group_hash, group_files in image_hashes.items():
                    if abs(group_hash - img_hash) <= threshold:
                        group_files.append(file_path)
                        found_group = True
                        break
                
                if not found_group:
                    image_hashes[img_hash] = [file_path]

        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    for i, (group_hash, group_files) in enumerate(image_hashes.items()):
        group_folder_path = os.path.join(output_directory, f"group_{i + 1}")
        os.makedirs(group_folder_path, exist_ok=True)

        for file_path in group_files:
            shutil.move(file_path, os.path.join(group_folder_path, os.path.basename(file_path)))