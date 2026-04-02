import tkinter as kt

root=kt.Tk()
root.geometry("300x200")
img=kt.PhotoImage(file="Black.png")
label=kt.Label(root,image=img)
label.image=img
label.pack()
root.mainloop()