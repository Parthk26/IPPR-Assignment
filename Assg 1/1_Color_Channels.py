from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "corridor.jpg"
image = Image.open(image_path)
image_array = np.array(image)
height, width, channels = image_array.shape

red_channel_image = np.empty_like(image_array)
green_channel_image = np.empty_like(image_array)
blue_channel_image = np.empty_like(image_array)

for i in range(height):
    for j in range(width):
        for k in range(channels):
            if(k != 0):
                red_channel_image[i, j, k] = 0
            else:
                red_channel_image[i, j, k] = image_array[i, j, k]

            if(k != 1):
                green_channel_image[i, j, k] = 0
            else:
                green_channel_image[i, j, k] = image_array[i, j, k]

            if(k != 2):
                blue_channel_image[i, j, k] = 0
            else:
                blue_channel_image[i, j, k] = image_array[i, j, k]

fig, axs = plt.subplots(2, 2)
axs = axs.flatten()

image_arrays = [image_array, red_channel_image, green_channel_image, blue_channel_image]
titles = ["Original Image", "Red Channel Image", "Green Channel Image", "Blue Channel Image"]

for i, ax in enumerate(axs):
    ax.imshow(image_arrays[i].astype(np.uint8))
    ax.axis('off')
    ax.set_title(titles[i])

plt.tight_layout()
plt.show()

