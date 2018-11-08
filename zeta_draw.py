import sys
sys.path.append("modules")
import func_py as f
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#-------------------------------------

# How big the data is
size=250

# How strict the process is
limit=100

# How wide to see
scale=10

#-------------------------------------
print("size =",size)
print("limit =",limit)
print("scale =",scale)

np.set_printoptions(threshold=np.inf)

x = np.linspace(-scale, scale, size)
y = np.linspace(-scale, scale, size)
xl=len(x)
yl=len(y)

a=np.zeros((xl,yl),dtype = np.float)
# Generate Datas
for i in range(xl):
    for j in range(yl):
        a[j][i] = abs(f.zeta(x[i]+y[j]*1j,limit))
    #print(i)
    f.progress(i+1,size)

np.savetxt("zeta results/txt/zeta_"+str(size)+"_"+str(limit)+"_"+str(scale)+".txt", a, delimiter=',')

#-------------------------------------

ax = plt.figure()
plt.xticks([-0.5,size-0.5],[-scale,scale])
plt.yticks([-0.5,size-0.5],[-scale,scale])
plt.xlim((-0.5, size-0.5))
plt.ylim((-0.5, size-0.5))
plt.imshow(a, interpolation='nearest', norm=colors.LogNorm(), cmap="Blues", origin='lower')
cbar=plt.colorbar()
cbar.set_ticks([1,10,100])
plt.savefig("zeta results/pics/zeta_"+str(size)+"_"+str(limit)+"_"+str(scale)+".png")
plt.show()
