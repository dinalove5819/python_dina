def sumFunc(user):
    print(user+"님. 두 숫자를 입력하세요.")
    num1 = int(input("정수1 ==> "))
    num2 = int(input("정수2 ==> "))
    num3 = int(input("정수3 ==> "))
    hap = num1+ num2+ num3
    return hap

hap = sumFunc("A")
print("결과: ", hap)
hap = sumFunc("B")
print("결과: ", hap)
hap = sumFunc("C")
print("결과: ", hap)