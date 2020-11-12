print('----------- packing -------------')
#packing  은 tuple로만 가능하다.
t = 10, 20, 30, 'python'
print(t, type(t))

print('----------- unpacking -------------')

a, b, c, d = t           # 갯수가 맞아야 된다. 많든 적든 오류남.
print(a, b, c, d)

print('----------- unpacking 확장-------------')

t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b, type(a), type(b))

*a, b = t
print(a, b)

a, *b, c = t
print(a, b ,c)

