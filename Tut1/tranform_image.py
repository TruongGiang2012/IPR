from PIL import Image, ImageOps

def rotate_and_flip_image(input_path, output_path):
    
    image = Image.open(input_path)

    # Rotate 90 degrees
    rotated_90_image = image.rotate(90)
    rotated_90_image.save(output_path + '_rotated_90.jpg')

    # Rotate 180 degrees
    rotated_180_image = image.rotate(180)
    rotated_180_image.save(output_path + '_rotated_180.jpg')

    # Horizontal flip
    flipped_horizontal_image = ImageOps.mirror(image)
    flipped_horizontal_image.save(output_path + '_flipped_horizontal.jpg')

    # Vertical flip
    flipped_vertical_image = image.transpose(Image.Transpose.ROTATE_180)
    flipped_vertical_image.save(output_path + '_flipped_vertical.jpg')

    
    image.close()

    print(f"Image transformations completed and saved to {output_path}")

rotate_and_flip_image('image.jpg', 'transformed')
