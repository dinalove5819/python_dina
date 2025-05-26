import tkinter

##전역 변수
tmr = 0

## 함수 선언
def countup():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, countup)

## 메인함수
root = tkinter.Tk()
root.title("타이머")
root.geometry("300x200")
label = tkinter.Label(font=("궁서체",80))
label.pack()
root.after(1000, countup)
root.mainloop()