x, y = map(float, input().split())

if x == 0 and y == 0:
    print('Origem')
elif x > 0 and (y > 0 or y < 0):
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
elif x < 0 and (y > 0 or y < 0):
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')
elif (x > 0 or x < 0) and y == 0:
    print('Eixo X')
elif x == 0 and (y > 0 or y < 0):
    print('Eixo Y')