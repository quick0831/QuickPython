# For data bases
# With matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

# ----------------------------------------------------

file = "mand_1000_5000"

data = np.loadtxt("mand results/"+file+".txt", dtype="int", comments="#", delimiter=",", unpack=False)

# ----------------------------------------------------
k=len(data)

ax = plt.figure()

plt.xticks(())
plt.yticks(())
plt.xlim((-0.5, k-0.5))
plt.ylim((0, k))
plt.imshow(data, interpolation='nearest', norm=colors.LogNorm(vmin=1, vmax=k), cmap="PuBu_r", origin='lower')
#plt.colorbar()
plt.savefig("mand results/pics/"+file+".png")
plt.show()

"""
k=""
for j in range(5000):
    k=k+data[j][0:5000]
    if j != 4999:
        k=k+","
"""