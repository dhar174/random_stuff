from matplotlib import pyplot as plt
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) *(1-sigmoid (x))


plt.plot(input, sigmoid(input), c="r")
