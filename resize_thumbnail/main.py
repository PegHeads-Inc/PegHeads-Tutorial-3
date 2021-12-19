from PIL import Image
import os

# Update the path to your images folder
images_folder = ""

images = [img for img in os.listdir(images_folder) if img.endswith(("png"))]
for image in images:
    img = Image.open(f"{images_folder}/{image}")

    # Image cannot be resized if it is smaller than the thumbnail size 
    img.thumbnail((600, 600))

    img.save(f"resized_{image}", "png")
    print(f"{image} was resized")
