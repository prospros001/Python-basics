# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

a  = input('입력>  ')
revers = ''

for a1 in a:
    revers = a1 + revers
print(revers)

