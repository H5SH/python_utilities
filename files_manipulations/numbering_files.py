import os
import glob


def number_files(directory, extension):
    # Change to the specified directory
    os.chdir(directory)
    
    # Find all .png files in the directory
    png_files = glob.glob(f'*.{extension}')
    
    # Sort files to ensure consistent renaming order
    png_files.sort()
    
    # Rename each file
    for index, filename in enumerate(png_files):
        new_name = f"{index + 1}.{extension}"
        os.rename(filename, new_name)
        print(f"Renamed {filename} to {new_name}")


# Specify the directory containing the image extension and files
img_extensions = 'jpg'
img_directory_path = 'C:/H5SH/companies/data_unfolding/wiresDitection/all_images'
txt_directory_path = 'new_train\labels'
# rename_files(img_directory_path, img_extensions)


