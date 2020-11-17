# 문제3.

# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

# s = s.replace(',', '').replace('.', '').upper()
# words = s.split(' ')
# words_results = list(set(words))
# words_results.sort(key=str)
#
# for word in words_results:
#     print("{0}:{1}".format(word, words.count(word)))




a = s.upper()
b = a.replace(',', '').replace('.', '').replace('\n', '')
count = b.split()
count1 =[]
for v in count:
    if v not in count1:
        count1.append(v)

count1.sort(key=str)
ans2 =[]

for ans1 in count1:
    ans2.append(ans1)
    print(ans1)
# print(ans2)

cnt = []

for z in count:
    cnt.append(count.count(z))

for ans
print(f'%s : %s 개' % (ans2, cnt))


