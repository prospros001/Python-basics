# 문제1. 다음 세 개의 리스트가 있을 때,
#
subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']
#
# 3형식 문장을 모두 출력해 보세요
# 실행 결과:
#
# I Play Hockey.
# I Play Football.
# I Love Hockey.
# I Love Football.
# You Play Hockey.
# You Play Football.
# You Love Hockey.
# You Love Football.

# for i in range(len(subjs)):
#     for j in range(len(verbs)):
#         for k in range(len(objs)):
#             sentence = "%s %s %s." % (subjs[i], verbs[j], objs[k])
#             print(sentence)




for a in subs:
    for b in verbs:
        for c in objs:
            print(f'{a} {b} {c}.')