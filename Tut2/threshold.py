import cv2
import matplotlib.pyplot as plt 

image_path = 'image.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()

threshold_value = 127
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

plt.imshow(binary_image, cmap='binary')
plt.title('Binary Image')
plt.show()