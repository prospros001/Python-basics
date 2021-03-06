# 문제2. range() 함수와 유사한 frange() 함수를 작성해 보세요.
# frange() 함수는 실수 리스트를 반환합니다.
# 실행 결과:
#
# [0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 0.9999999999999999, 1.0999999999999999, 1.2, 1.3, 1.4000000000000001, 1.5000000000000002, 1.6000000000000003, 1.7000000000000004, 1.8000000000000005, 1.9000000000000006]
# [1.0, 1.1, 1.2000000000000002, 1.3000000000000003, 1.4000000000000004, 1.5000000000000004, 1.6000000000000005, 1.7000000000000006, 1.8000000000000007, 1.9000000000000008]
# [1.0, 1.5, 2.0, 2.5]

# def frange(val, base=0.0, step=0.1):
#     results = []
#
#     if val < base:
#         start = val
#         stop = base
#     else:
#         start = base
#         stop = val
#
#     while start < stop:
#         results.append(start)
#         start += step
#
#     return results
#
#
# print(frange(2))
# print(frange(1.0, 2.0))
# print(frange(1.0, 3.0, 0.5))

def frange(num, step=0.1, end=1):
    results = []
    for a in range(end):
        results.append(num)
        num = num + step
    return results


print(frange(0.0, 0.1, 20))
print(frange(1.0, 0.1, 10))
print(frange(1.0, 0.5, 4))

