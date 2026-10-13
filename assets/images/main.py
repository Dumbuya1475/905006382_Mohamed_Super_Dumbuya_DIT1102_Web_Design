import os

# Path to your folder
# folder_path = r"C:\Users\YourName\Pictures\MyImages"
# folder_path = r"C:\Users\dumbu\Desktop\devProjects\dbc-website\public\Maleria"
folder_path = r"C:/Users/msdumbuya/Desktop/html/assets/images"

# Image extensions to rename
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")

# Get all image files
files = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith(image_extensions)
]

# Sort files for consistent numbering
files.sort()

# Rename images
for index, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)

    extension = os.path.splitext(filename)[1]
    new_name = f"image{index}{extension}"
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)
    print(f"{filename} -> {new_name}")

print("Done! All images have been renamed.")