# 문제6.
# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권,
# 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.

# 실행결과
# 금액: 67879

# 50000원 : 1개
# 10000원 : 1개
# 5000원: 1개
# 1000원: 2개
# 500원: 1개
# 100원: 3개
# 50원:1개
# 10원:2개
# 5원:1개
# 1원:4개

# import sys
#
# money = input('금액을 입력하세요: ')
# if money.isdigit() is False:
#     print('금액을 입력하세요')
#     sys.exit(0)
#
# money = int(money)
# for won in [50000, 10000, 5000, 1000, 500, 100, 50, 10, 50, 1]:
#     count = money // won
#     money -= count*won
#     print('{0}원: {1}개'.format(won, count))



money = input('금액: ')
m = int(money)
lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

for a in lst:
    ge = m // a
    m = m % a
    print(f'{a}원 : ' + str(ge) + '개')

