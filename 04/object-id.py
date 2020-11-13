# object ID
import sys

i1 = 10
i2 = 10

print(hex(id(i1)), hex(id(i2)))

i1 = 123649264891623962193462896429388749
i2 = 123649264891623962193462896429388749
print(hex(id(i1)), hex(id(i2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

# 가변 아이디는 다르다.
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

print(i1 is i2)
print(l1 is l2)
print(s1 is s2)

# ??
t1 = (1, 2, 3, 4)
t2 = (1, 2, 3, 4)
print(sys.getrefcount(t1), sys.getrefcount(t2))
print(t1 is t2)

