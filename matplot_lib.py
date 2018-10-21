import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x*x + x + 1
y1=3*x+1

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y,label="2x^2+x+1")
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 1))
plt.ylim((-2, 4))
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.xticks([-1,0,1],["a","$b$","c d"])
plt.yticks([-1,0,1])

axis = plt.gca()
axis.spines["top"].set_color("none")
axis.spines["right"].set_color("none")
# top,bottom,left,right

axis.spines["bottom"].set_position(("data", 0))
axis.spines["left"].set_position(("data", 0))
# outward,axes,data

plt.legend(loc="upper right")

plt.show()