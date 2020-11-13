# 레퍼런스 카운트
import sys

x = object()
print(type(x))

print(sys.getrefcount(x))       # x, sys 두개가 레퍼카운트 2개다

y = x

print(sys.getrefcount(y))       # x,y, sys 두개가 레퍼카운트 2개다

# 레퍼런스 값
del x               # x 는 symbol table 에서 사라진다.
print(sys.getrefcount(y))
# print(x)



