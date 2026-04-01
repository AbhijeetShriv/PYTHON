import tkinter

game=tkinter.Tk()

game.geometry("300x400")
game.minsize(100,200)
game.maxsize(800,500)
label_dem=tkinter.Label(text="GAME WILL LAUNCH SOON")
label_dem.pack()
game.mainloop()