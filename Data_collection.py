import os
import glob
import random
import matplotlib.pyplot as plt
from PIL import Image


DATA_PATH = "dataset/ui_cn_d/417/Camera_files"
NUM_IMAGES = 20


image_paths = glob.glob(os.path.join(DATA_PATH, "*.png"))

if len(image_paths) == 0:
    raise ValueError("No images found. Check DATA_PATH.")

print("Total images found:", len(image_paths))


num_images = min(NUM_IMAGES, len(image_paths))
selected_images = random.sample(image_paths, num_images)

rows = 4
cols = 5

plt.figure(figsize=(18, 12))

for i, img_path in enumerate(selected_images):
    img = Image.open(img_path).convert("RGB")

    plt.subplot(rows, cols, i + 1)
    plt.imshow(img)
    plt.title(os.path.basename(img_path), fontsize=8)
    plt.axis("off")

plt.tight_layout()
plt.show()
