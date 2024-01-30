from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "corridor.jpg"
image = Image.open(image_path)
image_array = np.array(image)
height, width, channels = image_array.shape

negative_image = np.empty_like(image_array)
green_channel_image = np.empty_like(image_array)
blue_channel_image = np.empty_like(image_array)

for i in range(height):
    for j in range(width):
        for k in range(channels):
            negative_image[i, j, k] = np.clip(255 - image_array[i, j, k], 0, 255)

fig, axs = plt.subplots(1, 2)
axs = axs.flatten()

image_arrays = [image_array, negative_image, ]
titles = ["Original Image", "Negative Image", ]

for i, ax in enumerate(axs):
    ax.imshow(image_arrays[i].astype(np.uint8))
    ax.axis('off')
    ax.set_title(titles[i])

plt.tight_layout()
plt.show()

