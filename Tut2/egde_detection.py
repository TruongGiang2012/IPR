import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Sobel operator in both x and y directions
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradients
magnitude = np.sqrt(sobelx**2 + sobely**2)

# Threshold the magnitude to identify edges
threshold_value = 100
edges = cv2.threshold(magnitude, threshold_value, 255, cv2.THRESH_BINARY)[1]

# Display the result
plt.imshow(edges, cmap='gray')
plt.title('Edges Detected')
plt.axis('off')
plt.show()
