# 다음의 세개의 라인은 hello world 문자열을 화면에 출력한다.
# print("hello world") - CTRL + / (여러줄 주석처리)
# print("hello world")
a = 10
b = 20
c = 30

if a < b:
    # 들여쓰기 조심하기
    # 새로운 자식블록이 생기면 (조건문, 반복문, 함수정의)
    # 반드시 들여쓰기로 블록이 구분해야 한다.
    print(a)
    print('big')
    if a + 1 == 2:
        print(a + 1)
        print(a + 2)

print('end')