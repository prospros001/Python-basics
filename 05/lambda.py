print('============== lambda : 익명함수 ==============')
# 입력받아서 출력이 있는 함수를  lamda로 만들수 있다.

# 일반 함수
# def blah(x):
#     return x * 2
#
# for i in range(10):
#     print(f'{i}:{blah(i)}')

# lambda 함수 ( x => x * 2)(i)
for i in range(10):
    print(f'{i}:{(lambda x: 2*x)(i)}')















