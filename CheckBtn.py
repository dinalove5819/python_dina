import tkinter
import random
import tkinter.messagebox

root = tkinter.Tk()
root.title("캔버스 만들기")

result = [
    "전생에 고양이었을 가능성은 매우 낮습니다.",
    "보통 사람입니다.",
    "특별히 이상한 곳은 없습니다.",
    "꽤 고양이 다운 구석이 있습니다.",
    "고양이와 비슷한 성격 같습니다.",
    "고양이와 근접한 성격입니다.",
    "전생에 고양이었을지도 모릅니다.",
    "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]

#체크버튼 클릭시
def chkBtnClick():
    numchcek = 0
    if cvalue1.get() == True:
        numchcek = 0
        print("체크 되었습니다.")
    else:
        print("체크가 해제 되었습니다.")

#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

def click_btn():
    label["text"]=random.choice(["대길","중길","소길","흉"])
    text.insert(tkinter.END,label["text"+"\n"])

#캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse=tkinter.Label(root,text=",",font=("맑은고딕",10))
labelMouse.pack()

#캔버스 내 이미지 생성
bgimg=tkinter.PhotoImage(file="mina.png")
canvas.create_image(400,300,image=bgimg)

textFiled = tkinter.Text()
textFiled.place(x=330,y=50,width=420,height=300)

root.mainloop()