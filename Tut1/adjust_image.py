from PIL import Image, ImageEnhance

def adjust_brightness_contrast(input_path, output_path, brightness_factor, contrast_factor):
    image = Image.open(input_path)

    # Adjust brightness 
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(brightness_factor)

    # Adjust contrast
    enhancer = ImageEnhance.Contrast(brightened_image)
    adjusted_image = enhancer.enhance(contrast_factor)

    adjusted_image.save(output_path)

    image.close()

    print(f"Image adjusted successfully and saved to {output_path}")

# Set the factors for adjusting
brightness_increase_factor = 1.5
contrast_increase_factor = 1.5

brightness_decrease_factor = 0.7
contrast_decrease_factor = 0.7

# Adjust brightness and contrast
adjust_brightness_contrast('image.jpg','image_increase.jpg', brightness_increase_factor, contrast_increase_factor)
adjust_brightness_contrast('image.jpg','image_decrease.jpg', brightness_decrease_factor, contrast_decrease_factor)