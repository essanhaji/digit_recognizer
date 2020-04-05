from correlation import compute_correlation_similarity_score
from sorensen import compute_sorensen_similarity_score
from jaccard import compute_jaccard_similarity_score
from digit_Comparator import Digit_Comparator
from picture import Picture
from my_modul import clear
import numpy as np


# to clear the console
clear()

# create Digit_Comparator class instance
my_comparator = Digit_Comparator()

# create array of pictures class instance
pictures_array = np.array([])

for i in range(len(my_comparator.digits.images)):
    pic = Picture(i, my_comparator.digits.target[i], my_comparator.digits.images[i])
    pictures_array = np.append(pictures_array, pic)

# print(pictures_array[9].show())

# the the request image
initial_image = pictures_array[4]

for picture in pictures_array:
    """
    you can change compute_correlation_similarity_score 
    by
    compute_jaccard_similarity_score
    or 
    compute_sorensen_similarity_score
    """

    picture.temps = compute_correlation_similarity_score(initial_image.vector, picture.vector)

pictures_array.sort()

# pictures_array = pictures_array[::-1]

for picture in pictures_array[0:50]:
    print(picture.temps)

my_comparator.disply_list_of_images(pictures_array[0:50])

