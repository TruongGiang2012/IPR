import cv2
import numpy as np

def resize_and_threshold(image_path, new_width, new_height, threshold_value):
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display original image
    cv2.imshow('Original Image', image)

    # Display resized image
    cv2.imshow('Resized Image', resized_image)

    # Display binary thresholded image
    cv2.imshow('Binary Thresholded Image', binary_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save resized and thresholded images (optional)
    cv2.imwrite('resized_image.jpg', resized_image)
    cv2.imwrite('binary_thresholded_image.jpg', binary_image)

# Example usage
if __name__ == "__main__":
    image_path = 'image.jpg' 
    new_width = 400
    new_height = 300
    threshold_value = 127

    resize_and_threshold(image_path, new_width, new_height, threshold_value)
