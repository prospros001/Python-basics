# 객체의 대소 비교
print(1 > 3)
print(2 < 4)
print(1 >= 3)
print(1 <= 4)
print(1 == 3)
print(1 != 3)

# 복합관계식
# 0 < a < 10

a = 4
print(0 < a and a < 10)      # 기존 프로그램
print(0 < a < 10)            # 파이썬에서 가능

# 수치형 이외의 다른 타입 비교
print('abcde' > 'abc')
print('aac' > 'abc')
print([1, 2, 3] < [1, 2, 4])
print((1, 2, 3) < (1, 2, 4))
print(id(a))

# 동질성  ==
# 통일성  is
a = 20
b = 20
c = a
print(a == b)
print(a is b)
print(b is c)
print(id(a))
print(id(b))

