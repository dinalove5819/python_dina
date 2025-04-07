import tkinter
import random
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title("캔버스 만들기")

#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

def click_btn():
    label["text"]=random.choice(["대길","중길","소길","흉"])

#캔버스 생성
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()

#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse=tkinter.Label(root,text=",",font=("맑은고딕",10))
labelMouse.pack()

#캔버스 내 이미지 생성
#bgimg=tkinter.PhotoImage(file="miko.png")
beimg=ImageTk.PhotoImage(Image.open('miko.png'))
canvas.create_image(400,300,image=beimg)

label = tkinter.Label(root,text=",",font=("맑은고딕",120))
label.place(x=380, y=60)

button = tkinter.Button(root,text="제비뽑기",font=("맑은 고딕",36),command=click_btn)
button.place(x=360, y=400)

root.mainloop()