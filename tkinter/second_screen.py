import tkinter as tk

window = tk.Tk()
window.title("Quick")
window.geometry("80x80")

t=tk.StringVar()
t.set("False")
v=False
def hit():
    global v
    v = not v
    if v:
        t.set("True")
    else:
        t.set("False")
text=tk.Label(window,textvariable=t,bg="yellow",width=10,height=2)
text.pack()
bt=tk.Button(window,text="Hit me!",width=10,height=2,command=hit)
bt.pack()

window.mainloop()