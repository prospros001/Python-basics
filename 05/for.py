print('----------- for loop 기본 -------------')

a = ['cat', 'cow', 'tiger']

for animal in a:
    print(animal, end='  ')
else:
    print(' ')

print('----------- 복합 자료형의 for loop -------------')
l1 = [('둘리', 10), ('마이클', 20), ('또치', 10)]

for t in l1:
#    print(f'이름 : {t[0]}, 나이:{t1}')     # 사용가능
    print('이름 :%s ,  나이:%d' % t)

for name, age in l1:
    print(f'이름 : {name}, 나이:{age}')

