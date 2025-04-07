import tkinter
root = tkinter.Tk()
root.title("캔버스 만들기")

#캔버스 생성
canvas = tkinter.Canvas(root, width=400, height=600, bg="#c4bee2")
canvas.pack()

#캔버스 내 이미지 생성
bgimg=tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300,image=bgimg)


root.mainloop()