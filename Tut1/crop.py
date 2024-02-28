from PIL import Image

def crop_image(input_path, output_path, box):
    image = Image.open(input_path)

    cropped_image = image.crop(box)

    cropped_image.save(output_path)

    image.close()

    print(f"Image cropped successfully and saved to {output_path}")

crop_box = (100, 50, 400, 300)

crop_image('image.jpg', 'cropped_image.jpg', crop_box)