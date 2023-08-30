import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()