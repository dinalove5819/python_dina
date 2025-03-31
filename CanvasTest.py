import tkinter
root = tkinter.Tk()
root.title("캔버스 만들기")
canvas = tkinter.Canvas(root, width=400, height=600, bg="#c4bee2")

bgimg=tkinter.PhotoImage(file="miko.png")

canvas.pack()
root.mainloop()