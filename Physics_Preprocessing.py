import os
import cv2
import random
import matplotlib.pyplot as plt

input_folder = r"dataset/ui_cn_d/417/Camera_files"
output_folder = r"preprocessed"
os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_resized = cv2.resize(img_gray, (640, 480))
        
        save_path = os.path.join(output_folder, filename)
        cv2.imwrite(save_path, img_resized)

print("Preprocessing complete. Images saved to 'preprocessed' folder.")

all_images = [f for f in os.listdir(output_folder) if f.endswith(".png")]


num_images = min(20, len(all_images))

random_images = random.sample(all_images, num_images)
plt.figure(figsize=(15, 10))

for i, img_name in enumerate(random_images):
    img_path = os.path.join(output_folder, img_name)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    plt.subplot(4, 5, i + 1)
    plt.imshow(img, cmap='gray')
    #plt.title(img_name)
    plt.axis('off')

plt.tight_layout()
plt.show()
