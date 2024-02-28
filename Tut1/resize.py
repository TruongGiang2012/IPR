from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):

    image = Image.open(input_path)

    resized_image = image.resize((new_width, new_height))

    resized_image.save(output_path)

    print(f"Resized image saved as {output_path}")

resize_image('image.jpg', 'resized_image.jpg', 800, 600)