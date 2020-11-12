print('----------- zip -------------')
# zip() 함수 사용 예

s1 = ['foo', 'bar', 'baz']
s2 = ['one', 'two', 'three', 'four']

z1 = zip(s1, s2)
print(z1, type(z1))

print('----------- 순회 -------------')
for t in z1:
    print(t, type(z1))
print('----------- 순회2 -------------')
z = zip(s1, s2)
for a, b in z:
    print(a, b)




