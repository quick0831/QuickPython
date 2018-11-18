import tkinter as tk
win=tk.Tk()
win.title("Enter Something!")
win.geometry("300x200")

def insert_point():
    var = u.get()
    t.insert('insert',var)

def insert_end():
    var = u.get()
    t.insert('end',var)

b1 = tk.Button(win,text="insert point",width=15,height=2,command=insert_point)
b1.pack()

b2 = tk.Button(win,text="insert end",command=insert_end)
b2.pack()

u=tk.Entry(win,show="")
u.pack()
p=tk.Entry(win,show="●")
p.pack()
t=tk.Text(win,height=2)
t.pack()

win.mainloop()