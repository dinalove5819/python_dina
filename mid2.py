print("##택배를 보내기 위한 정보를 입력하세요.##")
name=input("받는사람:==>")
address=input("주소:==>")
weight=float(input("무게(g):==>"))

shipping_fee=weight*5

print(f"받는사람:{name}")
print(f"주소:{address}")
print(f"무게(g){weight}")
print(f"배송비{shipping_fee}원")