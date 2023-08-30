{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "759a8380",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    " \n",
    " \n",
    "def add_salt_and_pepper_noise(image, noise_ratio=0.07):\n",
    "    noisy_image = image.copy()\n",
    "    h, w, c = noisy_image.shape\n",
    "    noisy_pixels = int(h * w * noise_ratio)\n",
    " \n",
    "    for _ in range(noisy_pixels):\n",
    "        row, col = np.random.randint(0, h), np.random.randint(0, w)\n",
    "        if np.random.rand() < 0.5:\n",
    "            noisy_image[row, col] = [0, 0, 0] \n",
    "        else:\n",
    "            noisy_image[row, col] = [255, 255, 255]\n",
    " \n",
    "    return noisy_image\n",
    " \n",
    "original_image = cv2.imread('3.png')\n",
    " \n",
    "noisy_image = add_salt_and_pepper_noise(original_image, noise_ratio=0.07)\n",
    " \n",
    "cv2.imshow(\"Original Image\", original_image)\n",
    "cv2.imshow(\"Noisy Image (Salt and Pepper)\", noisy_image)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2efb5420",
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
