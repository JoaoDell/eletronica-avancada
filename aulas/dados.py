import numpy as np
import matplotlib.pyplot as plt

fase1 = np.array([2.41, 7.16, 15.33, 27.1, 45.2, 51.2, 73.2])
freq1 = np.array([0.835, 2.05, 4.43, 8.16, 16.02, 20.45, 51.8])

fase2 = np.array([9.17, 40.8, 45.38, 70.57, 19.75])
freq2 = np.array([1.159, 5.068, 5.72, 10.603, 2.387])

plt.xlabel("freq (kHz)")
plt.ylabel("fase")
plt.scatter(freq1, fase1)
plt.scatter(freq2, fase2)
plt.grid()
plt.show()