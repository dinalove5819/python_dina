def func2():
     global hap
     num1 = 1             #지역변수 (함수 안에 선언 된 변수)가 우선
     result = 100 + num1  #읽기는 가능
     hap = result         #쓰기는 불가능
     return result

hap = 0
num1 = 10
func2()
print(hap)