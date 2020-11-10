# 정수형

a = 23
b = 20 + 3
# print(a, type(a))
# print(b, isinstance(b, int))
# print(b, isinstance(b, bool))

# 2진수, 10진수, 8진수, 16진수
c = 0b1101 #0b넣으면 2진수
print(c)

d = 0o23 #0o 넣으면 8진수
print(d)

e = 0x23 #0x 넣으면 16진수
print(e)

# python 3.xx에서 큰수도 int로 표시된다.
f = 2**1024
print(f, type(f))
print(f.bit_length())

# 변환함수
# print(oct(38)) #8진수
# print(hex(38)) #16진수
# print(bin(38)) #2진수



# a = 23
# print(type(a))
# print(isinstance(a,int))
#
# b = 0b1101
# c = 0o23
# d = 0x23
#
# print(a, b, c, d)
#
# e = 2**1024
# print(type(e))
# print(e)