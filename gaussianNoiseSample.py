{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a4bf7a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    " \n",
    "def add_gaussian_noise(image, mean=0, std=25):\n",
    "    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)\n",
    "    noisy_image = cv2.add(image, noise)\n",
    "    return noisy_image\n",
    " \n",
    "original_image = cv2.imread('3.png')\n",
    " \n",
    "noisy_image = add_gaussian_noise(original_image, mean=0, std=25)\n",
    " \n",
    "cv2.imshow(\"Original Image\", original_image)\n",
    "cv2.imshow(\"Noisy Image\", noisy_image)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a16cefff",
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
