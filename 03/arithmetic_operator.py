# 사칙연산

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 / 3.0)
print(2. / 3)

# # // (몫연산), **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# divmod() 함수
t = divmod(2, 3)
print(t, type(t))
a, b = divmod(2, 3)
print(a, b)

# 연산자 우선
# - (마이너스 부호) : 단항연산자
# + - * / : 이항연산자
# 우선순위
# 1. -
# 2. * /
# 3. + -
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

# 결합순서
# 1. ->   : + - * /
# 2. <-   : +(부호) -(부호),  **
print(2**3**4)
print((2**3)**4)
print(2**(3**4))