import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Task 1: Compute and display the histogram
plt.hist(image.ravel(), bins=256, range=[0,256])
plt.title('Image Intensity Histogram')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.show()

# Task 2: Apply histogram equalization to enhance contrast
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()
