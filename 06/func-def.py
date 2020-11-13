print('----------- 함수 정의 -------------')

def dummy():            # 아무것도 안하는 함수
    pass

def func1():
    print('Hello World')

def func2(name):         # 입력만 있는 함수
    print('Hello  ' + name)

def func3():             # 출력만 있는 함수
    return 'Hello World'

def times(a, b):         # 입 출력이 있는 함수
    return a * b

print('----------- 결 과 -------------')
dummy()
func1()
func2('안대혁')
s = func3()
n = times(2, 3)
print(s, n)

print('----------- 여러 값을 반환할 수 있다 -------------')

def func4():
    return 10, 20       # tuple auto packing을 통해 튜플 객체 하나를 반환한다

t = func4()             # tuple auto packing을 통해 반환된 튜플 객체를 여러 변수에 대입할수 있다.
print(t)

print('----------- 함수도 객체다. -------------')
print(func1)
print(type(func1))
print(id(func1))
f = func1()         #func1() 실행결과를 f에 넣는다.
print(f)
f = func1
print(f)
f()


print('----------- 함수도 객체다. -------------')

