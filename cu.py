import tkinter as tk
from tkinter import messagebox

# 상품 정보 (구입 가격, 판매 가격)
products = {
    "캔커피":(500,1800),
    "삼각김밥":(900,1400),
    "바나나 우유":(800,1500),
    "도시락":(3500,4000),
    "콜라":(700,1500),
    "새우깡":(1000,2000)
}

# GUI 생성
root = tk.Tk()
root.title("CU")
root.geometry("960x540")

# 레이블 생성
labels = ["캔 커피", "삼각김밥", "바나나 우유", "도시락", "콜라", "새우깡"]
tk.Label(root, text="판매 수량").grid(row=0, column=1)
tk.Label(root, text="구매 수량").grid(row=0, column=2)

# 입력 필드 저장할 딕셔너리
sell_entries = {}
buy_entries = {}

# 입력 필드 생성
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i + 1, column=0)
    sell_entries[label] = tk.Entry(root, width=10)
    sell_entries[label].grid(row=i + 1, column=1)
    buy_entries[label] = tk.Entry(root, width=10)
    buy_entries[label].grid(row=i + 1, column=2)

# 계산 함수
def calculate_sales():
    sales_total = 0
    
    for label in labels:
        buy_qty = int(buy_entries[label].get() or 0)
        sell_qty = int(sell_entries[label].get() or 0)
        
        buy_price, sell_price = products[label]
        
        sales_total = sales_total - (buy_price * buy_qty)  # 구입 비용 차감
        sales_total = sales_total + (sell_price * sell_qty)  # 판매 수익 추가
    
    messagebox.showinfo("결과", f"오늘 총 매출액은 {sales_total}원 입니다.")

# 계산버튼
tk.Button(root, text="계산", command=calculate_sales).grid(row=len(labels) + 1, columnspan=3)

root.mainloop