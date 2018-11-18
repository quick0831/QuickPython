import tkinter as tk

window = tk.Tk()
window.title("Quick")
window.geometry("500x400")

text=tk.Label(window,text="Hi!",bg="yellow",width=5,height=2)
text.pack()

window.mainloop()