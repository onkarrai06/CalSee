import cv2
import numpy as np

def preprocess_image(image):
    # Image resizing
    resized_image = cv2.resize(image, (416, 416), interpolation=cv2.INTER_CUBIC)

    # Denoising the images
    denoised_image = cv2.fastNlMeansDenoisingColored(resized_image, h=3, hColor=10)

    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(denoised_image, -1, kernel)

    return sharpened_image
