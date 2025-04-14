
# 실습 1
# 팩토리얼 계산기: 1부터 N까지의 곱
N=5
res = 1
for i in range(1,N+1,1):
    res = res * i
#print(res)

#연습1
#1000 - 2000 사이에서 홀수의 합을 구하는 프로그램

hap=0
for i in range(1001,2001,2): #1001부터 2001까지 홀수만 반복
    hap += i
#print("1000에서 2000까지의 홀수의 합:", hap)

#중첩 for문
for i in range(0,3,1):
    for k in range(0,2,1):
        print("중첩 for문입니다")
    pass

#실습2
#2단부터 9단까지 구구단을 출력하는 구구단 계산기
for num1 in range(2,10,1): #단
    for num2 in range(1,10,1): #곱해지는 수
        print(num1, "X", num2, "=\t", num1*num2)
    #print("")

#while문
while(True):
    num1 = int(input("숫자1 ===> "))
    #num1 이 0이면 반복문 종료
    if num1 == 0:
        break
    num2 = int(input("숫자2 ===> "))
    res = num1+num2
    print(num1, "+", num2, "=", num1 + num2)

#연습2
#1부터 100까지 더하되 4의 배수는 더하지 않음
#3의 배수도 더하지 않음
res = 0
for i in range(1,101,1):
    if i % 4 == 0:
        continue
    elif i % 3 == 0:
    res = res + i
    print (res)




