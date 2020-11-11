# 한줄 문자열 리터럴
s1 = 'Hello World'
s2 = "Hello World"
print(s1, s2, type(s1), type(s2))

# 여러줄 문자열 리터럴
# s3 = 'Hello\nWorld'
s3 = '''Hello
World
'''
print(s3)

# 여러줄 주석을 대신하여 사용할 수 있다.
'''
주석1
주석2
주석3
'''

# escape 문자열(\붙어있는 문자)
print('----------- escape -------------')
print('Hello\nWorld')
print('I say \'Hello World\'')
print("I say 'Hello World'")
print("둘리\t010-0000-0000")

print('----------- 문자열 연산: 길이 -------------')
print(len(s1))

# 문자열 연산
print('----------- 문자열 연산: 반복 -------------')
str1 = 'First String'
str2 = 'Second String'

str3 = str1 * 3
print(str3)

print('----------- 문자열 연산: 인덱싱 -------------')
print(str1[0], str1[2], str1[3], str1[11])
# IndexError: string index out of range
# print(str1[12])

print('----------- 문자열 연산: 연결 -------------')
str4 = str1 + ' ' + str2
print(str4)

# 리터럴을 연결할 때에는 + 생략가능
str5 = 'hello' '   ' 'world'
print(str5)

# 문자열 객체와 정수객체는  + 연산을 할수없다.
name = '둘리'
age = 10
# print(name + age)  -> 오류
print(name + str(age))

print('----------- 문자열 연산: in, not in -------------')
print("S" in str1)
print("S" not in str2)

print('----------- 문자열 객체는 변경할수 없다(immutable) -------------')
# str1[0] = 'f'
# print(str1)

print('----------- 문자열 연산: 슬라이싱 -------------')

print('----------- 문자열 연산: 객체 함수-------------')
# 대소문자 관련 함수
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())     # 대소문자를 바꾼다.
print(s.capitalize())   # 가장 앞만 대문자로
print(s.title())        # 단어 앞글자만 대문자

# 검색 관련 함수
s = 'I Like Python, I Like Deep Learning Also'
print(s.count("Like"))
print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("AI"))               # find()함수는 못찾으면 -1처리
print(s.rfind("Like"))

try :
    print(s.index("AI"))
except ValueError as e:
    print('index() 함수는 발견하지 못하면 예외가 발생한다.')

print(s.rindex("Like"))
print(s.startswith("i Like"))
print(s.endswith("Also"))
print(s.endswith("Python", 0, 13))

# 편집 및 치환
s = '        spam and ham         '
print('---' + s.strip() + '-----')        #전후 공백 없앤다
print('---' + s.rstrip() + '-----')        #오른쪽 공백 없앤다
print('---' + s.lstrip() + '-----')        #왼쪽 공백 없앤다

s = '<><><abc><><defg><><>'
print('---' + s.strip('<>') + '-----')
print(s.replace('<>', ''))

# 분리
s = 'one:two:three'
r = s.split(':')
print(r, type(r))


print('----------- 문자열 연산: 포맷팅 -------------')


