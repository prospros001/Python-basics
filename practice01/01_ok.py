# 문제1.
# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

num = input('수를 입력하세요:')

test = num.isdigit()

if test == False :
     print('정수가 아닙니다.')
else :
    a = int(num)

    if a % 3 == 0 :
        print('3의 배수 입니다.')
    else :
        print('3의 배수가 아닙니다.')
