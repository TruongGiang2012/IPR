from PIL import Image
import matplotlib.pyplot as plt

def load_and_display_image(image_path):
    image = Image.open(image_path)
    image.show()

    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
load_and_display_image('image.jpg')