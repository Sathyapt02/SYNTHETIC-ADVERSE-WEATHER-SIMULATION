import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("Performance/PSNR.txt")

frame_size = data[:, 0]
cga_kd = data[:, 1]
wgan_lstm = data[:, 2]
vgg16 = data[:, 3]

x = np.arange(len(frame_size))
width = 0.25

plt.figure(figsize=(10,6))

bars1 = plt.bar(x - width, cga_kd, width,
                label="CGA-KD",
                color="#1B9E77")

bars2 = plt.bar(x, wgan_lstm, width,
                label="WGAN-LSTM [1]",
                color="#D95F02")

bars3 = plt.bar(x + width, vgg16, width,
                label="VGG16 Transfer Learning [2]",
                color="#7570B3")

plt.xlabel("Frame Size (MB)", fontsize=13, fontweight='bold')
plt.ylabel("PSNR (dB)", fontsize=13, fontweight='bold')
plt.title("PSNR Comparison for Different Frame Sizes",
          fontsize=15, fontweight='bold')

plt.xticks(x, frame_size, fontsize=11, fontweight='bold')
plt.yticks(fontsize=11, fontweight='bold')

legend = plt.legend(loc='upper center',
                    bbox_to_anchor=(0.5, -0.15),
                    ncol=3,
                    frameon=False,
                    prop={'weight':'bold', 'size':11})


plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()

plt.savefig("psnr_comparison.png", dpi=300, bbox_inches='tight')

plt.show()
