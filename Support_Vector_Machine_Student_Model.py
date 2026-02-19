import os
import glob
import random
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import models, transforms
from sklearn import svm
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

DATA_ROOT = "dataset/ui_cn_d"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

CLASSES = sorted([
    folder for folder in os.listdir(DATA_ROOT)
    if os.path.isdir(os.path.join(DATA_ROOT, folder))
])

NUM_CLASSES = len(CLASSES)

if NUM_CLASSES < 2:
    raise ValueError("Need at least 2 scene folders for classification.")

print("Detected Classes (Scenes):", CLASSES)
print("Loading ResNet50 teacher...")

teacher = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
teacher = nn.Sequential(*list(teacher.children())[:-1])
teacher.to(DEVICE)
teacher.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

features = []
labels = []
image_paths = []

print("Extracting teacher features...")

with torch.no_grad():
    for class_idx, scene in enumerate(CLASSES):

        scene_path = os.path.join(DATA_ROOT, scene, "Camera_files")

        if not os.path.exists(scene_path):
            print(f"Skipping {scene} (no Camera_files folder)")
            continue

        image_files = glob.glob(os.path.join(scene_path, "*.png"))
        print(f"{scene} → {len(image_files)} images")

        for img_path in image_files:

            try:
                img = Image.open(img_path).convert("RGB")
                img_tensor = transform(img).unsqueeze(0).to(DEVICE)

                feat = teacher(img_tensor)
                feat = feat.view(feat.size(0), -1)

                features.append(feat.cpu().numpy())
                labels.append(class_idx)
                image_paths.append(img_path)

            except:
                continue

if len(features) == 0:
    raise ValueError("No images found in dataset.")

features = np.vstack(features)
labels = np.array(labels)

print("Feature Shape:", features.shape)

X_train, X_test, y_train, y_test, train_paths, test_paths = train_test_split(
    features,
    labels,
    image_paths,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


print("Training SVM student...")
student_model = svm.SVC(
    kernel='rbf',
    C=10,
    gamma='scale',
    probability=True
)

student_model.fit(X_train, y_train)

y_pred = student_model.predict(X_test)
y_prob = student_model.predict_proba(X_test)



def plot_test_images_with_predictions(num_images=20):

    num_images = min(num_images, len(test_paths))
    indices = random.sample(range(len(test_paths)), num_images)

    rows = 4
    cols = 5

    plt.figure(figsize=(18, 12))

    for i, idx in enumerate(indices):
        img = Image.open(test_paths[idx]).convert("RGB")

        plt.subplot(rows, cols, i + 1)
        plt.imshow(img)
        plt.axis("off")

        confidence = np.max(y_prob[idx])
        pred_label = CLASSES[y_pred[idx]]
        true_label = CLASSES[y_test[idx]]

        color = "green" if y_pred[idx] == y_test[idx] else "red"

        plt.title(
            f"P: {pred_label}\nT: {true_label}\nConf: {confidence:.2f}",
            fontsize=8,
            color=color
        )

    plt.tight_layout()
    plt.show()

plot_test_images_with_predictions(20)

joblib.dump(student_model, "student_svm_model.pkl")
joblib.dump(scaler, "feature_scaler.pkl")

print("Model and scaler saved successfully.")
