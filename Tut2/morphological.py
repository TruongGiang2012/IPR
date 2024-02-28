import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image in grayscale
image_path = 'image.jpg'  # Replace with your image path
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert it to a binary image
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(binary_image, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(binary_image, kernel, iterations=1)

# Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

# Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Display results
titles = ['Original Binary Image', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [binary_image, erosion, dilation, opening, closing]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()