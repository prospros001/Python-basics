print('----------- 생성 -------------')
s = {1, 2, 3}
print(s, type(s))

print('----------- 기본 연산 -------------')
print(len(s))
print(2 in s)
print(10 not in s)

print('---- 사용예 : list의 중복성 제거 ----')
word_list = ['a', 'hello', 'java', 'python', 'python', 'ai', 'hello', 'ai']
words = set(word_list)
print(words, type(words))
word_list2 = list(words)
print(word_list2, type(word_list2))

for w in words:
    count = word_list.count(w)
    print(f'{w}:{count}')

print('---- 객체함수 ----')
s.add(7)
print(s)

s.add(2)   #중복안된다.
print(s)

s.discard(2)
print(s)

s.remove(1)
print(s)

s.discard(10)
print(s)

try:
    s.remove(10)
except KeyError as e:
    print('remove는 discard와 다르게 없는 원소 제거시 예외 발생')

s.update({6, 7, 8})  # 추가할때 사용
print(s)

s.clear()
print(s)

print('---- 객체함수 : 수학 ----')
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30, 40, 50}

s3 = s1.union(s2)  # 합집합
print(s3)

s4 = s1.intersection(s2)  #교집합
print(s4)

s5 = s1.difference(s2)    # 차집합
print(s5)

s6 = s1.symmetric_difference(s2)    # 대칭차
print(s6)

