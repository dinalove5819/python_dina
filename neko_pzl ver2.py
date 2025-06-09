import tkinter
import random
import time
from tkinter import messagebox

index = 0
timer = 0
score = 0
hisc = 1000
difficulty = 0
tsugi = 0
last_placement_time = time.time()
placements = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

neko = []
check = []
for i in range(10):
    neko.append([0] * 12)  # Changed to 12 columns
    check.append([0] * 12)

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def save_hisc():
    with open("hisc.txt", "w") as file:
        file.write(str(hisc))

def load_hisc():
    global hisc
    try:
        with open("hisc.txt", "r") as file:
            hisc = int(file.read())
    except FileNotFoundError:
        hisc = 1000

def draw_neko():
    cvs.delete("NEKO")  # Remove old blocks
    for y in range(10):
        for x in range(12):  # Adjusted to 12 columns
            if neko[y][x] > 0:  # Draw blocks if they are present
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(12):  # Adjusted to 12 columns
            check[y][x] = neko[y][x]

    # Horizontal, Vertical, and Square Checks
    for y in range(1, 9):
        for x in range(12):
            if check[y][x] > 0:
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    for y in range(10):
        for x in range(1, 11):  # Adjusted to 12 columns
            if check[y][x] > 0:
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

    for y in range(1, 9):
        for x in range(1, 11):
            if check[y][x] > 0:
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

    # Detecting squares
    for y in range(9):
        for x in range(11):
            if check[y][x] > 0 and check[y + 1][x] == check[y][x] and check[y][x + 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                neko[y][x] = 7
                neko[y + 1][x] = 7
                neko[y][x + 1] = 7
                neko[y + 1][x + 1] = 7

def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(12):  # Adjusted to 12 columns
            if neko[y][x] == 7:
                neko[y][x] = 0  # Clear block
                num += 1  # Increment destroyed blocks count
    return num

def drop_neko():
    flg = False
    for y in range(8, -1, -1):
        for x in range(12):  # Adjusted to 12 columns
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(12):  # Adjusted to 12 columns
        if neko[0][x] > 0:  # Game Over if there is a block on top row
            return True
    return False

def set_neko():
    for x in range(12):  # Adjusted to 12 columns
        neko[0][x] = random.randint(0, difficulty)  # Add new block

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, score, hisc, difficulty, tsugi, last_placement_time, placements
    global cursor_x, cursor_y, mouse_c

    if index == 0:  # Title screen
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1
        mouse_c = 0

    elif index == 1:  # Difficulty selection
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x < 456 and 384 < mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x < 456 and 528 < mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x < 456 and 672 < mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(10):
                for x in range(12):  # Adjusted to 12 columns
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2

    elif index == 2:  # Drop block
        if drop_neko() == False:
            index = 3
        draw_neko()

    elif index == 3:  # Check blocks
        check_neko()
        draw_neko()
        index = 4

    elif index == 4:  # Destroy matching blocks
        sc = sweep_neko()
        score += sc * difficulty * 2
        if score > hisc:
            hisc = score
        if score > hisc:
            save_hisc()
        if sc > 0:
            index = 2
        else:
            if not over_neko():
                tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()

    elif index == 5:  # Wait for input
        if 24 <= mouse_x < 24 + 72 * 12 and 24 <= mouse_y < 24 + 72 * 10:
            cursor_x = int((mouse_x - 24) / 72)
            cursor_y = int((mouse_y - 24) / 72)
            if mouse_c == 1:
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                placements += 1
                last_placement_time = time.time()
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()

    elif index == 6:  # Game Over
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0

    # Display information
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO")

    # Display timer
    draw_txt(f"Time: {int(time.time() - last_placement_time)}", 300, 100, 32, "green", "INFO")

    root.after(100, game_main)

# Load high score at the beginning
load_hisc()

root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)

cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
]

cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()