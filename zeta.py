import sys
sys.path.append("modules")
import functions as f
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 1000)
z = f.zeta(1/2+t*1j,50000)
x = z.real
y = ( z - x ) / 1j
y = y.real
plt.plot(x, y)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()