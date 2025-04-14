import tkinter
import tkinter.messagebox as msgbox
import random

# 좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"] = str(x) + "," + str(y)

# 게임 시도 버튼 클릭 시
def click_btnCheck():
    global count, btnCheck, successGame

    # 입력값 유효성 검사
    if (entryLec1.get() == "") or (entryLec2.get() == "") or (entryLec3.get() == ""):
        return
    elif (len(entryLec1.get()) != 1) or (len(entryLec2.get()) != 1) or (len(entryLec3.get()) != 1):
        return
    elif (not entryLec1.get().isdigit()) or (not entryLec2.get().isdigit()) or (not entryLec3.get().isdigit()):
        return

    # 버튼 비활성화 및 시도 횟수 증가
    btnCheck["state"] = "disabled"
    count += 1
    successGame = False

    # 사용자 입력 처리
    user = [entryLec1.get(), entryLec2.get(), entryLec3.get()]
    if len(set(user)) != 3:
        msgbox.showwarning("경고", "서로 다른 숫자를 입력하세요.")
        return

    # 정답 리스트로 변환
    answer_list = list(answer)

    # 스트라이크 & 볼 계산
    strike = 0
    ball = 0
    for i in range(3):
        if user[i] == answer_list[i]:
            strike += 1
        elif user[i] in answer_list:
            ball += 1

    output_str = str(strike) + "S " + str(ball) + "B"
    btnCheck["text"] = output_str

    # 정답이면 successGame
    if strike == 3:
        successGame = True

    # 게임 종료 조건
    if count == 10:
        response = msgbox.showerror("종료", "아쉽게도 모든 기회를 사용했습니다.\n정답은 " + str(answer) + " 입니다.")
        if response:
            root.destroy()
    elif successGame:
        response = msgbox.showinfo("성공", "정답입니다!\n정답은 " + str(answer) + " 입니다.")
        if response:
            root.destroy()
    else:
        nextGame()

# 다음 입력창 세팅
def nextGame():
    global entryLec1, entryLec2, entryLec3, btnCheck

    labelCount = tkinter.Label(root, text=str(count) + "회", font=("맑은 고딕", 10))
    labelCount.place(x=15, y=15 + count * 25)

    entryLec1 = tkinter.Entry(width=2)
    entryLec2 = tkinter.Entry(width=2)
    entryLec3 = tkinter.Entry(width=2)

    entryLec1.place(x=60, y=15 + count * 25)
    entryLec2.place(x=90, y=15 + count * 25)
    entryLec3.place(x=120, y=15 + count * 25)

    btnCheck = tkinter.Button(root, text="확인", font=("Times New Roman", 10), command=click_btnCheck)
    btnCheck.place(x=150, y=15 + count * 25, width=70, height=20)

# 초기화
root = tkinter.Tk()
root.title("숫자 야구 게임")
root.geometry("250x300")

root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕", 10))
labelMouse.place(x=0, y=270)

# 시도 횟수 초기화
count = 1

# 중복 없는 세 자리 숫자 생성
while True:
    answer = str(random.randint(100, 999))
    if len(set(answer)) == 3:
        break
print("정답(디버그용):", answer)  # 실제 게임에선 지워도 됨

# 첫 입력창 세팅
nextGame()

# 메인 루프
root.mainloop()
