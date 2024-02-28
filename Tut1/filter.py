from PIL import Image, ImageFilter

def apply_filter(input_path, output_path):
    image = Image.open(input_path)
    
    # Apply blur filter
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(output_path + '_blured.jpg')

    # Apply sharpen filter
    sharpened_image = image.filter(ImageFilter.SHARPEN)
    sharpened_image.save(output_path + '_sharpened.jpg')

    image.close()

    print(f"Filtering completed and saved to {output_path}")

apply_filter('image.jpg','filtered')