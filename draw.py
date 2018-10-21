# For data bases
# With matplotlib
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------

file = "mand results/mand_500_100.txt"

data = np.loadtxt(file, dtype="int", comments="#", delimiter=",", unpack=False)

# ----------------------------------------------------
k=len(data)

plt.xticks(())
plt.yticks(())
plt.xlim((-0.5, k-0.5))
plt.ylim((0, k))
plt.imshow(data, interpolation='nearest', cmap='jet', origin='lower')
plt.colorbar()
plt.show()

"""
k=""
for j in range(5000):
    k=k+data[j][0:5000]
    if j != 4999:
        k=k+","
"""