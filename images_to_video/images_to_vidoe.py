import os
import cv2

image_folder = ''

video_name = ''

images = [img for img in os.listdir(image_folder) if img.endswith('.jpg')]

images.sort()

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))

for image in images:
    video.writer(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

print(f"Video Saved As {video_name}")