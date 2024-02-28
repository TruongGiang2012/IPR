import cv2
import matplotlib.pyplot as plt

def display_images(before, after, title1="Before", title2="After"):
    """
    Helper function to display before and after images side by side
    """
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

# Load the low-contrast image
image_path = 'image.jpg'  # Make sure to change this to your image path
image = cv2.imread(image_path)

# Convert the image to grayscale for CLAHE
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a CLAHE object (Arguments are optional)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(gray_image)

# Convert the CLAHE output back to BGR to display with matplotlib
clahe_image_bgr = cv2.cvtColor(clahe_image, cv2.COLOR_GRAY2BGR)

# Display the original and CLAHE-enhanced images
display_images(image, clahe_image_bgr, "Original Image", "CLAHE Enhanced Image")
