# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

lst = []
count = 5
sum = 0

for c in range(count):
    n = input(f'[{c+1}]>')
    m = int(n)
    lst.append(m)
    # print(lst)

for t in lst:
    sum = sum + t

print('평균:' + str(sum/5))