import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image.jpg'  # Replace 'image.jpg' with your image file
image = cv2.imread(image_path)

# Task 1: Generate Gaussian and Laplacian pyramids
def generate_pyramids(image):
    # Generate Gaussian pyramid
    gaussian_pyramid = [image]
    for _ in range(5):  # Adjust the number of pyramid levels as needed
        image = cv2.pyrDown(image)
        gaussian_pyramid.append(image)

    # Generate Laplacian pyramid
    laplacian_pyramid = [gaussian_pyramid[-1]]
    for i in range(len(gaussian_pyramid) - 1, 0, -1):
        expanded = cv2.pyrUp(gaussian_pyramid[i])
        laplacian = cv2.subtract(gaussian_pyramid[i-1], expanded)
        laplacian_pyramid.append(laplacian)

    return gaussian_pyramid, laplacian_pyramid

gaussian_pyramid, laplacian_pyramid = generate_pyramids(image)

# Task 2: Explore image blending using pyramids
# Load another image for blending
image2_path = 'image2.jpg'  # Replace 'image2.jpg' with your second image file
image2 = cv2.imread(image2_path)

# Generate pyramids for the second image
gaussian_pyramid2, _ = generate_pyramids(image2)

# Blend images using pyramids
blended_pyramid = []
for level_img1, level_img2 in zip(laplacian_pyramid, gaussian_pyramid2):
    rows, cols, _ = level_img1.shape
    blended = np.hstack((level_img1[:, :cols//2], level_img2[:, cols//2:]))
    blended_pyramid.append(blended)

# Reconstruct the blended image from the blended pyramid
blended_image = blended_pyramid[0]
for i in range(1, len(blended_pyramid)):
    blended_image = cv2.pyrUp(blended_image)
    blended_image = cv2.add(blended_image, blended_pyramid[i])

# Display the original images and the blended image
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image 1')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Original Image 2')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
plt.title('Blended Image')
plt.axis('off')

plt.show()
