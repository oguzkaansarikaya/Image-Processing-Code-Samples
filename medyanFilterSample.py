{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "321bb720",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "img = cv2.imread('2.png')\n",
    "median = cv2.medianBlur (img, 5)\n",
    "compare = np.concatenate ((img, median), axis=1) #side by side comparison\n",
    "cv2.imshow('img', compare)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7fa78c3f",
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
