print('----------- 기본(default) 인수값(parameter) -------------')

def incr(a, step=1):
    return a + step

a = incr(10)
print(a)

a = incr(10, step=5)
print(a)

print('----------- 에러 -------------')

# def decr(step=1, 1):            #인수값 순서 바꾸면 안된다.
#     return a - step

print('----------- 키워드 인수값(keyword parameter-------------')
def area(width, height):
    return width * height

print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))
print(area(10, height=20))
# print(area(30, width=20))         #오류 난다 순서 바꾸고 명확한 이름지정없으면

print('----------- 가변 인수값-------------')
def func2(*arg):                # *로 가변인수 만든다
    print(arg)

func2(10, 20)
func2(10, 20, 30)
func2(10, 20, 30, 40)

def func3(a, *arg):                # *로 가변인수 만든다
    print(a, arg)

func3(10, 20)
func3(10, 20, 30)
func3(10, 20, 30, 40)

print('----------- 모든 인수를 sum-------------')

def sum2(*arg):
    s = 0
    for n in arg:
        s += n
    return s

print(sum2())
print(sum2(1,2))
print(sum2(1,2,3,4,5))
