import cv2
import os

# Update the path to your images folder
images_folder = ""

video_name = "video.avi"
images = [img for img in os.listdir(images_folder) if img.endswith(("png"))]
frame = cv2.imread(os.path.join(images_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(images_folder, image)))

cv2.destroyAllWindows()
video.release()
