from statistics import mean
import numpy as np
import matplotlib.pyplot as plt


def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))

    b = mean(ys) - m*mean(xs)
    return m, b


x = np.linspace(0,5,25)
y = np.random.rand(len(x))*2




m, b = best_fit_slope_and_intercept(x,y)



y_pred = (m*x)+b

plt.scatter(x, y)
plt.plot(x, y_pred)
print(np.random.rand(len(x))*2)
plt.title('Line Plot')
plt.xlabel('(cm)')
plt.ylabel('(cm)')
plt.show()
