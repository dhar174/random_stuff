import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,9,7,5])
x2 = tf.constant([8,3,4,2])


# Multiply
result = tf.multiply(x1, x2)

my_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
var = tf.Variable(my_tensor )


import numpy as np
import matplotlib.pyplot as plt


x = tf.Variable(2.0)

with tf.GradientTape() as tape:
  y = x**4


# dy = 2x * dx
dy_dx = tape.gradient(y, x)
dy_dx.numpy()



# Print the result
print(dy_dx.numpy())
