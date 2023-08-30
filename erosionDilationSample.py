{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04c7e7dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "img = cv2.imread('1.jpg', 0)\n",
    "kernel = np.ones((7,5), np. uint8)\n",
    "img_erosion = cv2.erode (img, kernel, iterations=1) \n",
    "img_dilation = cv2.dilate(img, kernel, iterations=1)\n",
    "cv2.imshow('Input', img)\n",
    "cv2.imshow('Erosion', img_erosion)\n",
    "cv2.imshow('Dilation', img_dilation)\n",
    "cv2.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52f785b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
