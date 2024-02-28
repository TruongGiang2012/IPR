import cv2 
import numpy as np
from PIL import Image

def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)

    grayscale_image = image.convert('L')

    grayscale_image.save(output_path)

    print(f"Grayscale image saved as {output_path}")

convert_to_grayscale('image.jpg', 'grayscale_image.jpg')

def apply_threshold(image_path, output_path, threshold_value):
    grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imwrite(output_path, binary_image)

    print(f"Binary image saved as {output_path} with threshold value {threshold_value}")

threshold_value = [100, 150, 200]

for threshold_value in threshold_value:
    output_path = f'binary_image_threshold_{threshold_value}.jpg'
    apply_threshold('grayscale_image.jpg', output_path, threshold_value)