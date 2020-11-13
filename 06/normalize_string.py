print('==================  normalize_string  ===================')
# 문자열 데이터를 분석(학습)하기 전 처리함수 만들기
# 1. 공백제거
# 2. 필요없는 문장, 부호 빼기
# 3. 대소문자 정리(Capitalize 처리)
# 4.
# 5.

import re

states = ['alabama', ' georgia!', 'georgis', 'FlOrIda', 'south carolina', 'West virginia?']

def clean_string(strings):
    result = []
    for string in strings:

        string = string.strip()                  # 1
        string = re.sub('[!@#?]', '', string)    # 2
        string = string.title()                  # 3

        result.append(string)

    return result

states = clean_string(states)
print(states)

print('==================  normalize_string 1 ===================')
# data -> f1() -> data2 -> f2() -> data3 -> f3() -> data3(final)

states = ['alabama', ' georgia!', 'georgis', 'FlOrIda', 'south carolina', 'West virginia?']

def title(s):
    return s.title()

def remove_specialch(s):
    return re.sub('[!@#?]', '', s)

def strip(s):
    return s.strip()

def clean_string(strings, *funcs):
    results =[]
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return None


states = clean_string(states, strip, remove_specialch, title)
print(states)