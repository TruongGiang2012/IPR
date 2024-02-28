import cv2
import matplotlib.pyplot as plt

# Function to display images
def display_images(before, after, title1="Before", title2="After"):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.title(title1)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(after, cv2.COLOR_BGR2RGB))
    plt.title(title2)
    plt.axis('off')
    
    plt.show()

# Load the image with salt-and-pepper noise
image_path = 'low_contrast_image.jpg'  # Change this to the path of your noisy image
image = cv2.imread(image_path)

# Apply a median filter
median_filtered = cv2.medianBlur(image, 5)  # The second parameter is the kernel size

# Display the original and median-filtered images
display_images(image, median_filtered, "Original Image", "Median Filtered Image")

# Apply a bilateral filter
bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)  # Diameter, SigmaColor, SigmaSpace

# Display the original and bilateral-filtered images
display_images(image, bilateral_filtered, "Original Image", "Bilateral Filtered Image")




