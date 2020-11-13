# global, local 심벌 테이블
g_a = 1
g_s = '둘리'

def g_f():
    l_a = 2
    l_s = '마이콜'
    print(locals())
print('======== Glovla Symbol Table VS Local Symble Table=========')
print(globals())
g_f()

print(g_a)
# 에러 : loacl symbol table은 함수가 실행되면 사라진다.
# print(l_a)

# 사용자 정의 함수
g_f.n ='hello'
g_f.i = 10
print(g_f.__dict__)

# 사용자 정의 클래스
class MyClass:
    x = 10
    y = 10
MyClass.z = 30
print(MyClass.__dict__)

o = MyClass()
print(o, type(o))