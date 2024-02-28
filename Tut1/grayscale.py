from PIL import Image, ImageDraw
import random

from PIL import Image

def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)

    grayscale_image = image.convert('L')

    grayscale_image.save(output_path)

    print(f"Grayscale image saved as {output_path}")

convert_to_grayscale('image.jpg', 'grayscale_image.jpg')