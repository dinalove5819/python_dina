import tkinter

#함수 영역
def main_proc():
    lable["text"] = "확인"
    root.after(100, main_proc)

def key_down():
    pass

#메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<key press>")
lable = tkinter.Label(font=("맑은 고딕",80))
lable.pack

main_proc()
root.mainloop()