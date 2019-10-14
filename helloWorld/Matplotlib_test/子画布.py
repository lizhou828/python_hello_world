import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100)

plt.subplot(221)
plt.plot(x, x)

plt.subplot(222)
plt.plot(x, -x)

plt.subplot(223)
plt.plot(x, x ** 2)

plt.subplot(224)
plt.plot(x, np.log(x))

plt.show()