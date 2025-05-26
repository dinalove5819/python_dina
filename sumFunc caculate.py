#함수 정의 부분
def calc(v1, v2, op):
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
         result = v1 - v2
    elif op == '*' :
         result = v1 * v2
    elif op == '/' :
         result = v1 / v2
    return result

#전역 변수 선언 부분
res = 0
v1, v2, oper = 0, 0, ""

#메인코드 부분
op = input("계산 입력(+, -, *, /):")
var1 = int(input("첫 번째 숫자 입력:"))
var2 = int(input("두 번째 숫자 입력:"))

res = calc(v1, v2, oper)
print("## 계산기 :", v1, op, v2, "=", res)