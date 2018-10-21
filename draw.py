# For data bases
# With matplotlib
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------

data = np.zeros((5000,5000))

# ----------------------------------------------------
"""
plt.xticks(())
plt.yticks(())
plt.xlim((-2, 1))
plt.ylim((-1.5, 1.5))
plt.imshow(data, interpolation='nearest', cmap='bone', origin='upper')
plt.show()
"""
"""
k=""
for j in range(5000):
    k=k+data[j][0:5000]
    if j != 4999:
        k=k+","
"""
np.set_printoptions(threshold=np.inf)
print(data)