from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "corridor.jpg"
image = Image.open(image_path)
image_array = np.array(image)
height, width, channels = image_array.shape

enhanced_image = np.empty_like(image_array)

to_enhance = int(input("Enter 0 for Red \n1 for Green\n2 for Blue \n(default is 0): "))
if not to_enhance:
    to_enhance = 0

for i in range(height):
    for j in range(width):
        for k in range(channels):
            if(k == to_enhance):
                enhanced_image[i, j, k] = np.clip(image_array[i, j, k] * 1.8, 0, 255)
            else:
                enhanced_image[i, j, k] = image_array[i, j, k]

fig, axs = plt.subplots(1, 2)
axs = axs.flatten()

image_arrays = [image_array, enhanced_image]
enhanced_image_title = f"Enhanced {['Red', 'Green', 'Blue'][to_enhance]} Image"
titles = ["Original Image", enhanced_image_title,]

for i, ax in enumerate(axs):
    ax.imshow(image_arrays[i].astype(np.uint8))
    ax.axis('off')
    ax.set_title(titles[i])

plt.tight_layout()
plt.show()

