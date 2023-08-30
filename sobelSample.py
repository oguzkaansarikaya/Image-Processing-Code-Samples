import cv2
import numpy as np

image = cv2.imread("1.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
sobel = np.uint8(sobel)

cv2.imwrite("sample.jpg", sobel)