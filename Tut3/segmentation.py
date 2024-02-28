import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image.jpg'  # Replace 'image.jpg' with your image file
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply morphological operations to remove noise
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# Sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0 but 1
markers = markers + 1

# Mark unknown region with 0
markers[unknown == 255] = 0

# Apply Watershed algorithm
markers = cv2.watershed(image, markers)
image_rgb[markers == -1] = [255, 0, 0]  # Mark watershed boundaries

# Display the segmented image
plt.imshow(image_rgb)
plt.title('Segmented Image with Watershed Algorithm')
plt.axis('off')
plt.show()
