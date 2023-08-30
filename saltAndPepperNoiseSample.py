import cv2
import numpy as np
 
 
def add_salt_and_pepper_noise(image, noise_ratio=0.07):
    noisy_image = image.copy()
    h, w, c = noisy_image.shape
    noisy_pixels = int(h * w * noise_ratio)
 
    for _ in range(noisy_pixels):
        row, col = np.random.randint(0, h), np.random.randint(0, w)
        if np.random.rand() < 0.5:
            noisy_image[row, col] = [0, 0, 0] 
        else:
            noisy_image[row, col] = [255, 255, 255]
 
    return noisy_image
 
original_image = cv2.imread('3.png')
 
noisy_image = add_salt_and_pepper_noise(original_image, noise_ratio=0.07)
 
cv2.imshow("Original Image", original_image)
cv2.imshow("Noisy Image (Salt and Pepper)", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()