import os
import shutil

source_dir = r"dataset/ui_cn_d/417"

semantic_folder = os.path.join(source_dir, "semantic_files")
other_folder = os.path.join(source_dir, "Camera_files")

os.makedirs(semantic_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.lower().endswith(".png"):
        file_path = os.path.join(source_dir, filename)

        if "semantic" in filename.lower():
            shutil.move(file_path, os.path.join(semantic_folder, filename))
        else:
            shutil.move(file_path, os.path.join(other_folder, filename))

print("Files split successfully!")
