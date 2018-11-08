import sys
sys.path.append("modules")
import func_py as f
#print(f.mand(0,0,500))
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#-------------------------------------

# How big the data is
size=500

# How strict the process is
limit=500

#-------------------------------------
print("size =",size)
print("limit =",limit)

np.set_printoptions(threshold=np.inf)

x = np.linspace(-2, 1, size)
y = np.linspace(-1.5, 1.5, size)
xl=len(x)
yl=len(y)

a=np.zeros((xl,yl),dtype = np.int)
# Generate Datas
for i in range(xl):
    for j in range(yl):
        a[j][i]=f.mand(x[i]+y[j]*1j,limit)
    #print(i)
    f.progress(i+1,size)

np.savetxt("mand results/2/mand_"+str(size)+"_"+str(limit)+".txt", a, delimiter=',', fmt="%d")

#-------------------------------------

ax = plt.figure()
plt.xticks(())
plt.yticks(())
plt.xlim((-0.5, size-0.5))
plt.ylim((0, size))
plt.imshow(a, interpolation='nearest', norm=colors.LogNorm(), cmap="autumn", origin='lower')
#plt.colorbar()
plt.savefig("mand results/pics/mand_"+str(size)+"_"+str(limit)+".png")
plt.show()
