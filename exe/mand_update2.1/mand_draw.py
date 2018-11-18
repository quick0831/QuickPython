#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
#sys.path.append("../../modules")
#print(f.mand(0,0,500))
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def mand(c,lim,pow=2):#Manderbrot set
    z=0+0j
    n=1
    while abs(z)<=2 and n<=lim:
        z=z**pow+c
        n+=1
        #print(n)
    return n
"""
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
"""
size=0
limit=0
#-------------------------------------

win=tk.Tk()
win.title("Mand")
win.geometry("200x130")

def hit():
    global size
    global limit
    size = int(m.get())
    limit = int(n.get())
    win.destroy()

tk.Label(win,text="How clear the picture is",width=30,height=1).pack()

m=tk.Entry(win,show="")
m.insert("end", "500")
m.pack()

tk.Label(win,text="How strict the process is",width=30,height=1).pack()

n=tk.Entry(win,show="")
n.insert("end", "250")
n.pack()

bt=tk.Button(win,text="I'm Finish!",width=10,height=1,command=hit)
bt.pack()

win.mainloop()

#-------------------------------------
"""
print("size =",size)
print("limit =",limit)
"""

if not os.path.isdir("../mand results"):
    os.mkdir("../mand results")

np.set_printoptions(threshold=np.inf)

x = np.linspace(-2, 2, size)
y = np.linspace(-2, 2, size)
xl=len(x)
yl=len(y)

#-------------------------------------
win2=tk.Tk()
win2.title("Hold on!")
win2.geometry("300x80")
tk.Label(win2,text="It might take a while",width=30,height=1).pack()
pgbar=ttk.Progressbar(win2,orient="horizontal",length=250,mode="determinate")
pgbar.pack()
pgbar["value"]=0
pgbar["maximum"]=size
tk.Label(win2,text="Data will be stored in folder \"mand results\"",width=40,height=1).pack()
def progress(count):
    pgbar["value"]=count
    pgbar.update()
#-------------------------------------

a=np.zeros((xl,yl),dtype = np.int)
# Generate Datas
for i in range(xl):
    for j in range(yl):
        a[j][i]=mand(x[i]+y[j]*1j,limit)
    #print(i)
    progress(i+1)#,size)

win2.destroy()

np.savetxt("../mand results/mand_"+str(size)+"_"+str(limit)+".txt", a, delimiter=',', fmt="%d")

#-------------------------------------

ax = plt.figure()
plt.xticks(())
plt.yticks(())
plt.xlim((-0.5, size-0.5))
plt.ylim((-0.5, size-0.5))
plt.imshow(a, interpolation='nearest', norm=colors.LogNorm(), cmap="autumn", origin='lower')
#plt.colorbar()
plt.savefig("../mand results/mand_"+str(size)+"_"+str(limit)+".png")
plt.show()