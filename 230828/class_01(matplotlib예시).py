import matplotlib.pyplot as plt
import numpy as np


# [예시]
# 01
data = [10,14,19,20,25]
plt.plot(data)
plt.show()

# 02-1
x = np.arange(-4.5,5,0.5)
# y = 2*x**2

# plt.plot(x)


x = np.arange(-4.5,5,0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 1/2*x**3 -10

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x, y3)
plt.show()

# 02-2
plt.plot(x, y1, x,y2, x, y3)
plt.show()

# 03
plt.plot(x,y1)

plt.figure()
plt.plot(x,y2)
plt.show()


