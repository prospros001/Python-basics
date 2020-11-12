# 문제4. 다음과 같이 출력되도록 구구단을 작성하세요(이중 for~in)

# for sec in range(1, 10):
#    print(1, '*', sec, '=', 1 * sec, '     ', 2, '*', sec, '=', 2 * sec, '     ', 3, '*', sec, '=', 3 * sec, '     ', 4, '*', sec, '=', 4 * sec, '     ', 5, '*', sec, '=', 5 * sec, '     ', 6, '*', sec, '=', 6 * sec, '     ', 7, '*', sec, '=', 7 * sec, '     ', 8, '*', sec, '=', 8 * sec, '     ', 9, '*', sec, '=', 9 * sec)

# for n in range(1, 10):
#     print(1, '*', sec, '=', 1 * sec, '     ', 2, '*', sec, '=', 2 * sec, '     ', 3, '*', sec, '=', 3 * sec)

# for fir in range(2, 10):
#     for scd in range(1, 10):
#         print(fir, scd, (fir * scd))


# for k in range(2, 10):
#     line = line + str("   # %d단 #   " %k)
# print(line)

for sec in range(1, 10):
    line = ''
    for fir in range(2, 10):
        line = line + str("%d * %d = %3d    " %(fir, sec, fir*sec))
    print(line)