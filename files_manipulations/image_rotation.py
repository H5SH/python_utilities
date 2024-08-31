from PIL import Image
import os


def rotate_and_save(img, save_path_prefix):
    for angle in [0, 90, 180, 270]:
        rotated_img = img.rotate(angle, expand=True)
        save_path = f"{save_path_prefix}_rotated_{angle}_Image.png"
        rotated_img.save(save_path)

save_directory = 'rotated_new_images'
images_directory = 'new_images'

def open_images_in_directory(directory):
    files = os.listdir(directory)
    image_files = [file for file in files if file.lower().endswith(('.jpg', 'jpeg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(directory, image_file)
        save_path = os.path.join(save_directory, os.path.splitext(image_file)[0]) 
        img = Image.open(image_path)
        rotate_and_save(img, save_path)


open_images_in_directory(images_directory)