print('----------- 생성 -------------')
d1 = {'basketball': 5, 'baseball': 9}
print(d1, type(d1))

d2 = dict()
print(d2, type(d2))

d3 = dict(one=1, two=2, three=3, four=4)
print(d3, type(d3))

d4 = dict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d4, type(d4))

print('----------- 접근 : 인덱스 대신 키로 접근 -------------')
print(d1['baseball'])

print('----------- *, + 연산은 지원하지 않는다 -------------')

# d1 + {'valleyabll': 6}
# d5 = d1 *2

print('----------- 크기 -------------')
print(len(d1))

print('----------- not, not in -------------')
print('soccer' in d1)
print('soccer' not in d1)

print('----------- 다양한 타입의 키를 사용할수 있다. -------------')
d6 = {}
print(d6)

d6['twenty'] = 20
d6[True] = 1
d6[10] = 'ten'
print(d6)

print('----------- 키는 변경가능한 타입을 사용할 수 없다. -------------')
# d6[[1, 2, 3]] = 6

print('----------- 객체함수: key() -------------')
k = d6.keys()
print(k, type(k))

print('----------- 객체함수: values() -------------')
v = d6.values()
print(v, type(v))

print('----------- 객체함수: items() -------------')
a = d6.items()
print(a, type(a))

print('----------- 객체함수: copy() -------------')
phones = {'둘리': '000-0000-0000', '마이콜': '111-1111-1111', '또치': '222-2222-2222'}
p = phones
print(phones)
print(p)
phones['도우너'] = '333-3333-3333'
print(phones)
print(p)

p = phones.copy()
print(phones)
print(p)
phones['홍길동'] = '444-444-4444'
print(phones)
print(p)

print('----------- 객체함수: get() -------------')
print(p.get('둘리'))
print(p['둘리'])
# print(p['고길동'])     -> 오류
print(p.get('고길동'))     # get 사용이유: 키가 없는 경우 none으로 반환 받을수있다.

print('----------- 객체함수: setDefault() -------------')
print(p.setdefault('고길동', '---'))       # 있으면 출력 없으면 뒤 값을 넣음

print('----------- 객체함수: pop() -------------')
print(p.pop('둘리'))
print(p)

print('----------- 객체함수: clear() -------------')
p.clear()
print(p)

print('----------- 순회 -------------')
d7 = {'c': 3, 'a': 1, 'b': 2}

for key in d7:
    print(key, end='  ')
else:
    print(' ')
for key in d7.keys():
    print(key, end='  ')
else:
    print(' ')

for key, value in d7.items():
    print(f'key={key}, values={value}')

