import cv2
import matplotlib.pyplot as plt

def display_image_in_actual_colors(img):
    """
    Helper function to display an image in its actual colors
    """
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Do not show axes to keep it clean
    plt.show()

def display_channels(title, channels, color_map=None):
    """
    Helper function to display each channel of an image
    """
    fig, axs = plt.subplots(1, len(channels), figsize=(20, 5))
    fig.suptitle(title)
    for i, channel in enumerate(channels):
        ax = axs[i] if len(channels) > 1 else axs
        c_map = 'gray' if color_map is None else color_map[i]
        ax.imshow(channel, cmap=c_map)
        ax.axis('off')
    plt.show()

# Load the image
image_path = 'download.jpg'  # Make sure to use your own image path
image = cv2.imread(image_path)

# Convert from RGB (actually BGR since OpenCV loads images as BGR) to HSV and YCbCr
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_ycbcr = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Display the original image
print("Original Image:")
display_image_in_actual_colors(image)

# Display the channels for HSV
print("HSV Channels:")
display_channels("HSV Channels", cv2.split(image_hsv))

# Display the channels for YCbCr
print("YCbCr Channels:")
display_channels("YCbCr Channels", cv2.split(image_ycbcr))

