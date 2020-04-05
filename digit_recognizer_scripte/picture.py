from digit_Comparator import Digit_Comparator
from sklearn import datasets
from PIL import Image
from my_modul import clear
import matplotlib.pyplot as plt
import numpy as np



class Picture:

    def __init__(self, id, label, image_color):
        self.id = id
        self.label = label
        self.image_color = image_color
        self.image_bw = self.to_black_and_white()
        self.vector = self.to_vector()
        self.descriptor = self.image_descriptor()
        self.temps = 0.0
        self.temps_additionnal = 0.0

    # image matrix to vector
    def to_vector(self):
        return np.array(self.image_bw).reshape(-1)

    # image color to black and white image
    def to_black_and_white(self):
        image_b_w = Image.fromarray(self.image_color)
        image_converted = image_b_w.convert('L')
        return np.array(image_converted)
    
    # image descriptor
    def image_descriptor(self):
        array = self.image_bw
        horz_proj = [np.count_nonzero(row) for row in array]
        img_trans = array.transpose()
        ver_proj = [np.count_nonzero(row) for row in img_trans]
        return horz_proj + ver_proj

    def show(self):
        print("=>> id\n{}".format(self.id))
        print("=>> label\n{}".format(self.label))
        print("=>> image_color\n{}".format(self.image_color))
        print("=>> image_bw\n{}".format(self.image_bw))
        print("=>> vector\n{}".format(self.vector))
        print("=>> descriptor\n{}".format(self.descriptor))
        print("=>> temps\n{}".format(self.temps))
        print("\n\n")

    def __eq__(self, other):
        return self.temps == other.temps and self.id == other.id

    def __lt__(self, other):
        return self.temps > other.temps



if __name__ == "__main__":
    
    clear()

    my_comparator = Digit_Comparator()

    pic = Picture(1, "1", my_comparator.digits.images[0])

    pic.show()