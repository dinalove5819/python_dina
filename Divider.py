import tkinter

#버튼 클릭하면 실행하는 함수
def btn_click():
    #값 입력(글자여서 숫자로 바꿔야 함)
    num1 = int(entry1.get())
    num2 = int(entry2.get())
   
   #라벨에 넣을 문자열
    str1 = ""+str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
    str2 = ""+str(num1)+"을(를) "+str(num2)+"(으)로 나눈 나머지는 "+str(num1%num2)+"입니다."

   #라벨 만들기(설명이 담긴 문자열 1,2)
    labelRes1 = tkinter.Label1(root,text=str1,font=("맑은고딕",10))
    labelRes1.place(x=21,y=86)
    
    labelRes1 = tkinter.Label1(root,text=str1,font=("맑은고딕",10))
    labelRes1.place(x=21,y=124)

#tkinter 기본문
root = tkinter.Tk()
root.title("산술 연산자")
root.geometry("400x300")

label1 = tkinter.Label(root, text="나눠 지는 수", font=("맑은 고딕",10))
label2 = tkinter.Label(root, text="나누는 수", font=("맑은 고딕",10))

label1.place(x=25,y=35)
label2.place(x=35,y=77)

#사용자가 값을 입력하는 란
entry1 = tkinter.Entry(width=8)
entry1.place(x=102,y=20)

entry2 = tkinter.Entry(width=8)
entry2.place(x=102,y=48)

btn = tkinter.Button(root,text="계산", font=("돋움",10),command=btn_click)
btn.place(x=200,y=200,width=32,height=32)

root.mianloop()