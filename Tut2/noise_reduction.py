import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image.jpg'
image = cv2.imread(image_path)

# Task 1: Add Gaussian noise to the image
mean = 0
std_dev = 25
noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)

# Task 2: Apply Gaussian filter to reduce noise
kernel_size = (5, 5)
sigma_x = 0
filtered_image = cv2.GaussianBlur(noisy_image, kernel_size, sigma_x)

# Display original image, noisy image, and filtered image
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Filtered Image')
plt.axis('off')

plt.show()
