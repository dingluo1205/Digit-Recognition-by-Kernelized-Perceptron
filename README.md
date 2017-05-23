# Digit-Recognition-by-Kernelized-Perceptron

### Overview: 

In this problem, I performed a digit recognition task, given an image of a handwritten digit and wish to predict what number it represents. 
This is a special case of an important area of language processing known as Optical Character Recognition (OCR). 
To simplify our goal, I used a binary classification between two relatively hard-to-distinguish numbers (specifically, predicting a '3' versus a '5'). 
Then, I implemented a kernelized version of the Perceptron algorithm and compared loss between different kernel functions.

### Data:

The digit images have been taken from the Kaggle competition. 
This data was originally from the MNIST database of handwritten digits, but was converted into a easier-to-use file format.
The data has also undergone some preprocessing. It has been filtered to just those datapoints whose labels are 3 or 5, 
which have then been relabeled to 1 and -1 respectively. Then, 1000-point samples have been created, 
named {validation.csv} and {test.csv}. The first column of these files is the label of each point, followed by the grayscale value of each pixel.

### Results:

#### Perceptron:

Use kernel $k_p^1(u,v) = u \cdot v + 1$ and run Perceptron for a single pass over the validation set with this kernel, and record the
average loss every 100 steps, plot the average loss L as a function of the number of steps T. 

L=[0.25,0.185,0.19,0.1725,0.168,0.1533,0.1428,0.1425,0.1311,0.13]


#### Polynomial kernel:

For the set d = [1, 3, 5, 7, 10, 15, 20], run Perceptron for a single pass over the validation
set with d, and plot the average loss over the validation set.

L=[0.13,0.025,0.008,0.013,0.022,0.03,0.02]

Conclusion: d=5 has the highest accuracy

#### Exponential kernel:

run Perceptron with both d=5 and 10 for a single pass over the testing set. Then report the average loss for every
100 steps.

L[d=5]=[0.55,0.545,0.513,0.5,0.496,0.5,0.503,0.505,0.4922,0.496]

L[d=10]=[0.55,0.535,0.527,0.497,0.486,0.487,0.477,0.467,0.462,0.465]
