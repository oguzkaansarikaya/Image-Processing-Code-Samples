import cv2
import numpy as np
img = cv2.imread('2.png')
median = cv2.medianBlur (img, 5)
compare = np.concatenate ((img, median), axis=1) #side by side comparison
cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows