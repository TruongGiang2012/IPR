import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image.jpg'  # Replace 'image.jpg' with your image file
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Harris Corner Detection algorithm
harris_corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold the corner response
threshold = 0.01 * harris_corners.max()
corner_image = np.zeros_like(image_rgb)
corner_image[harris_corners > threshold] = [255, 0, 0]  # Mark detected corners in red

# Display the original image with detected corners
plt.imshow(image_rgb)
plt.title('Original Image with Detected Corners')
plt.axis('off')
plt.show()

# Display the detected corners
plt.imshow(corner_image)
plt.title('Detected Corners')
plt.axis('off')
plt.show()
