# 문제10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
#     - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )

# while True:
#     number = input('숫자를 입력하세요:')
#     if number.isdigit() is False:
#         break
#
#     number = int(number)
#
#     s = 0
#     for n in range(number+1):
#         if number & 0x0001 ^ n & 0x0001 == 0:
#             s += n
#
#     print('결과 값: {0}'.format(s))



a = input('숫자를 입력하세요 : ')

num = int(a)
hol1 = 0
if num % 2 != 0 :
    for hol in range(1, num+1 , 2):
        hol1 += hol
    print(hol1)

else:
    for hol in range(2, num+1, 2):
        hol1 += hol
    print(hol1)


