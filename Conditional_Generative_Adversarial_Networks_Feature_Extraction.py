import os
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import random


image_folder = "preprocessed"
semantic_folder = "dataset/ui_cn_d/417/semantic_files"
batch_size = 32
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class AV_Dataset(Dataset):
    def __init__(self, image_folder, semantic_folder):
        self.image_folder = image_folder
        self.semantic_folder = semantic_folder
        
        self.image_files = sorted(
            [f for f in os.listdir(image_folder) if f.endswith(".png")]
        )

        self.img_transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor()
        ])

        self.sem_transform = transforms.Compose([
            transforms.Resize((256, 256), interpolation=Image.NEAREST),
            transforms.ToTensor()
        ])

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        rgb_name = self.image_files[idx]
        
        base_id = rgb_name.split("_")[0]

        semantic_name = f"{base_id}_semantic0.png"

        rgb_path = os.path.join(self.image_folder, rgb_name)
        semantic_path = os.path.join(self.semantic_folder, semantic_name)

        if not os.path.exists(semantic_path):
            raise FileNotFoundError(f"Missing semantic file: {semantic_path}")

        image = Image.open(rgb_path).convert("RGB")
        semantic = Image.open(semantic_path).convert("L")  # 🔥 FIXED

        image = self.img_transform(image)
        semantic = self.sem_transform(semantic)

        return image, semantic, rgb_name

class TeacherEncoder(nn.Module):
    def __init__(self, input_channels=3, condition_channels=1, feature_dim=256):
        super(TeacherEncoder, self).__init__()

        self.encoder = nn.Sequential(
            nn.Conv2d(input_channels + condition_channels, 64, 4, 2, 1),
            nn.ReLU(),
            nn.Conv2d(64, 128, 4, 2, 1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, feature_dim, 4, 2, 1),
            nn.BatchNorm2d(feature_dim),
            nn.ReLU()
        )

    def forward(self, x, condition):
        x = torch.cat([x, condition], dim=1)  
        features = self.encoder(x)
        return features

dataset = AV_Dataset(image_folder, semantic_folder)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)

print("Total Samples:", len(dataset))

model = TeacherEncoder().to(device)
model.eval()

all_features = []

with torch.no_grad():
    for images, semantics, filenames in dataloader:
        images = images.to(device)
        semantics = semantics.to(device)

        features = model(images, semantics)
        all_features.append(features.cpu())

print("Feature Extraction Complete")
print("Example Feature Shape:", all_features[0].shape)

torch.save(all_features, "teacher_features.pt")
print("Features saved as teacher_features.pt")

num_display = min(5, len(dataset))
indices = random.sample(range(len(dataset)), num_display)

plt.figure(figsize=(20, 8))

for i, idx in enumerate(indices):
    image, semantic, name = dataset[idx]

    image = image.permute(1, 2, 0).numpy()
    semantic = semantic.squeeze().numpy()
    
    plt.subplot(2, 5, i + 1)
    plt.imshow(image)
    plt.title(f"RGB\n{name}")
    plt.axis("off")
    
    plt.subplot(2, 5, i + 6)
    plt.imshow(semantic)
    plt.title("Semantic")
    plt.axis("off")

plt.tight_layout()
plt.show()
