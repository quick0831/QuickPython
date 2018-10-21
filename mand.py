import sys
sys.path.append("modules")
import functions as f
#print(f.mand(0,0,500))
import matplotlib.pyplot as plt
import numpy as np

#-------------------------------------

# How big the data is
size=10000

# How strict the process is
limit=500

#-------------------------------------

plt.figure(num=5)

np.set_printoptions(threshold=np.inf)

x = np.linspace(-2, 1, size)
y = np.linspace(-1.5, 1.5, size)
xl=len(x)
yl=len(y)

#plt.colorbar(mappable=1)
plt.xticks(())
plt.yticks(())
plt.xlim((-2, 1))
plt.ylim((-1.5, 1.5))

a=np.zeros((xl,yl),dtype = np.int)
# Generate Datas
for i in range(xl):
    for j in range(yl):
        a[j][i]=f.mand(x[i]+y[j]*1j,limit)
    #print(i)
    f.progress(i+1,size)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
#plt.show()

#np.set_printoptions(threshold=np.inf)
"""
print("[")
for j in range(yl):
    if j != yl-1:
        print(a[j][0:xl],",")
    else:
        print(a[j][0:xl],"]")
"""
#print(a)
# ----------------------------------------------
#file = open("Results.txt","w")
#dat = a.tostring()
#data = str(dat, encoding='utf-8')
#a.tofile("Results.txt")
np.savetxt("mand results/mand_"+str(size)+"_"+str(limit)+".txt", a, delimiter=',', fmt="%d")
#file.write(data)