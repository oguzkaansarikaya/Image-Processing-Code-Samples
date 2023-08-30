import cv2
import numpy as np

img = cv2.imread("1.jpg",0)
cv2.imshow("Original",img)
cv2.waitKey(0)

kernel = np.ones((5,5),dtype=np.uint8)

whiteNoise = np.random.randint(0,2,size=img.shape[:2])
whiteNoise = whiteNoise + img

opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
cv2.imshow("Opening",opening)
cv2.waitKey(0)