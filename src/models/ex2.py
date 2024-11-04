import numpy as np
from PIL import Image

image = Image.open("../../images/stork.png")
image_data = np.array(image)

print(image_data.shape)
print("---------------------------")

new_array = np.array([[1,2], [3,4]])
print(new_array * 2)
print("---------------------------")

sequence_data = np.arange(2, 14)
print(sequence_data)
print(sequence_data.shape)
print("---------------------------")
sequence_data=sequence_data.reshape(6,2)
print(sequence_data)
print(sequence_data.shape)
print("---------------------------")

print(image_data)
image_data[:, :, 2] = 0
print(image_data)

print("---------------------------")

np.mean(image_data)
np.min(image_data)
np.max(image_data)

processed_image = Image.fromarray(image_data)
processed_image.save("../../images/updated_image.png")



