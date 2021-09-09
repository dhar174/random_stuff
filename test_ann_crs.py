import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

import sklearn.datasets as datasets
from sklearn.datasets import make_blobs

epochs = 1000

samples = 1000

features = tf.keras.Input(shape=(4,))

x_train, y_train = make_blobs(n_samples=1000, centers=3, n_features=4)
x_test, y_test = make_blobs(n_samples=1000, centers=3, n_features=4)

print(x_train.shape)

print(x_train)
hidden = tf.keras.layers.Dense(3, activation=tf.nn.sigmoid)(features)
labels = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)(hidden)
model = tf.keras.Model(inputs = features, outputs = labels)
print(tf.__version__)

mae = tf.keras.losses.MeanAbsoluteError()

optimizer = tf.keras.optimizers.SGD(learning_rate = 1e-1)

x_sample = x_train[-500:]

y_sample = y_train[-500:]

model.compile(loss= mae, optimizer = optimizer)

print(x_train.shape)
history = model.fit(x_train,y_train, epochs = epochs )

print(history.history)



x,y = x_test,y_test
print(x)
results = model.evaluate(x, y, verbose = 1,steps = 1000, use_multiprocessing = True )
print("test loss, test acc:",results)

plt.plot(list(range(1, epochs+1)), history.history['loss'], 'r--')
plt.plot(10, results, 'bo')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show();
plt.subplot(5,5,1)
plt.xticks([])
plt.yticks([])
plt.grid(False)
#    plt.xlabel(labels[i])
#plt.show()

x = tf.convert_to_tensor(np.array(x_train), dtype=tf.float64)
print(x)
print(model(x).numpy())
