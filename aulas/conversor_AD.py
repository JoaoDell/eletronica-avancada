import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("scope_0.csv")

t = np.array(data["second"])
V = np.array(data["Volt"])
Dv = 10
plt.plot(t, Dv*V)
plt.grid()
plt.xlabel("t (s)")
plt.ylabel("V (V)")
plt.show()