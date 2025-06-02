import tkinter

#전역 변수
key = 0
cx = 400
cy = 300

#함수 영역
def main_proc():
    global cx, cy, key
    #lable["text"] = key
    if key =="Up":
        cx += cx + 20
    if key =="Down":
        cx -= cx - 20
    if key =="Left":
        cx = cx - 20
    if key =="Right":
        cx = cx + 20

    #변경된 위치의 경계를 확인
    if cy < 40 : cy = 40
    if cy > 600-40 : cy = 600-40
    if cx < 40 : cx = 40
    if cx < 800-40 : cx = 800-40

    #변경된 위치에 이미지를 옮김
    canvas.coords("춘식",cx,cy)
    key = 0
    root.after(100, main_proc)

def key_down(e):
    global key
    key = e.keysym #keycode

def key_up(e):
    global key
    key = e.keysym

#메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
#lable = tkinter.Label(font=("맑은 고딕",80))
#lable.pack()
canvas = tkinter.Canvas(width=800,height=600,bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file="춘식.png")
canvas.create_image(400,300, image=img)
canvas.coords("춘식",500,400)

main_proc()
root.mainloop()