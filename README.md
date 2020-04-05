# MNIST Dataset : Digit Recognizer



### python-mnist
This dataset is made up of 1797 8x8 images. Each image, like the one shown below, is of a hand-written digit. In order to utilize an 8x8 figure like this, we’d have to first transform it into a feature vector with length 64 [link](https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html).

- See [here](https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits) for more information about this dataset.


### Requirements
- Python 3.7 64bit



### Installation
- Get the package from PyPi :
- All requirement that you will need its exist in ``requirements.txt`` so you just need to run this command :

```
!pip install -r requirements.txt
```




### EMNIST
- Get EMNIST data :
```
print(__doc__)


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

from sklearn import datasets

import matplotlib.pyplot as plt

#Load the digits dataset
digits = datasets.load_digits()

#Display the first digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
```







### Test
Congratulation.

#### For Script Version
- Open the ```digit_recognizer_scripte/main.py``` and edit it as you want.<br><br>
![demo](digit_recognizer_scripte/demo.gif)

#### For Notebook Version
- Open the notebook ```digit_recognizer_notebook/main.ipynb``` and edit it as you want.<br/>
- [main.ipynb](digit_recognizer_notebook/main.ipynb)



## Authors
* **[El Houcine ES SANHAJI](https://essanhaji.github.io)** - *Initial work* - [essanhaji](https://github.com/essanhaji)




## Thank you.
