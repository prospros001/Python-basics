# 문제3.

# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

a = s.upper()
b = a.replace(',', '').replace('.', '').replace('\n', '')
count = b.split()
count1 =[]
for v in count:
    if v not in count1:
        count1.append(v)

count1.sort(key=str)

ans1 = []

for ans1 in count1:
    print(ans1)

cnt = []

for z in count:
    cnt.append(count.count(z))
print(cnt)

for w in ans1:
    print(f'{w}:{cnt} 개')


