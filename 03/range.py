print('----------- range -------------')

# seq = range(0, 10, 1)
seq = range(10)
print(seq, type(seq))

for i in seq :
    print(i, end='  ')
else:
    print('')

for i in range(5, 15):
    print(i, end='   ')
else:
    print('')

for i in range(0, 10, 2):
    print(i, end='   ')
else:
    print('')

for i in range(0, -10, -1):
    print(i, end='   ')
else:
    print('')

print('----------- 1~10 합구하기 -------------')
s = 0

for n in range(1, 11):
    s = s + n
#   s += n    -> 가능
print(s)

print('----------- break -------------')
for i in range(10):
    if i > 5 :
        break
    print(i, end="   ")
else:
    print('-- loop end --')

print('\n ----------- continue -------------')
for i in range(10):
    if i <= 5:
        continue
    print(i, end="   ")
else:
    print('-- loop end --')

print(' ----------- 삼각형1 -------------')
a = '*'
t = ''
for i in range(1, 6):
    t = i * a
    print(t)

print(' ----------- 삼각형2 -------------')
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end='')
    print('')



print(' ----------- 역 삼각형1 -------------')



print(' ----------- 역 삼각형2 -------------')
print(' ----------- 구구단 -------------')
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')

