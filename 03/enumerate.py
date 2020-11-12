print('----------- enumerate(번호 붙이기)-------------')

index = 1
for color in ['red', 'blue', 'yellow', 'gray']:
    print(f'{index} : {color}')
    index += 1
print('-------------------------------------------')

for i, color in enumerate(['red', 'blue', 'yellow', 'gray']):
    print(f'{i+1} : {color}')




