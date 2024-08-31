import os
from PIL import Image
import imagehash

def find_duplicates(directory):
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    try:
                        image = Image.open(f)
                        hash_value = str(imagehash.average_hash(image))
                        if hash_value in hashes:
                            duplicates.append(file_path)
                        else:
                            hashes[hash_value] = file_path
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")

    return duplicates


def delete_duplicates(duplicates):
    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"{duplicate} Deleted")

if __name__ == '__main__':
    directory = ''
    duplicates = find_duplicates(directory)
    if duplicates:
        delete_duplicates(duplicates)
    else:
        print("No Duplicates")