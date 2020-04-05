import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from PIL import Image
from my_modul import clear
from math import ceil, sqrt


class Digit_Comparator:

    def __init__(self):
        # Load the digits dataset
        self.digits = datasets.load_digits()
        # image matrix for test
        self.matrix_for_test = self.digits.images[0]

    # desply images in one figure
    def disply_list_of_images(self, image_list):
        plt.figure(figsize=(10, 10))
        i = 1
        for image in image_list:
            nbr = ceil(sqrt(len(image_list)))
            plt.subplot(nbr, nbr, i)
            plt.imshow(image.image_color, plt.cm.binary)  
            i += 1
        plt.show()

if __name__ == "__main__":

    clear()

    digit_comparator = Digit_Comparator()
    
    # test
    digit_comparator.disply_list_of_images(digit_comparator.digits.images[0:50])