import numpy as np
import matplotlib.pyplot as plt
A1 = np.array([10.9, 10.6, 10.9, 10.5, 10.5, 10.5, 10.5, 10.3, 10.3, 10.3, 10.3, 10.2])
A2 = np.array([10.7, 10.4, 10.1, 9.5, 8.7, 7.6, 6.4, 5.6, 4.3, 3.5, 2.5, 0.05])
w = np.array([10.62, 46.72, 86.15, 131.25, 192.32, 266.02, 349.77, 424.53, 581.2, 730.6, 1027.3, 10063.])
fase = np.array([2, 11, 21, 31, 41.96, 51.75, 61.8, 72.7, 81.3, 91.3, 106.3, 167.])

G = 20*np.log10(A2/A1)


plt.subplot(121)
plt.xlabel("freq (Hz)")
plt.ylabel("G")
plt.scatter(np.log10(w), G)
plt.grid()

plt.subplot(122)
plt.xlabel("freq (Hz)")
plt.ylabel("fase (°)")
plt.scatter(np.log10(w), fase)
plt.grid()

plt.show()

