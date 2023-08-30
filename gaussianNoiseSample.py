import cv2
import numpy as np
 
def add_gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image
 
original_image = cv2.imread('3.png')
 
noisy_image = add_gaussian_noise(original_image, mean=0, std=25)
 
cv2.imshow("Original Image", original_image)
cv2.imshow("Noisy Image", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()