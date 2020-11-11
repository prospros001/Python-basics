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

# for w in words:
#     count = word_list.count(w)
#     print(f'{w}:{count}')

print('---- 객체함수 ----')





