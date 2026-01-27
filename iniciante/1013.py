A, B, C = map(int, input().split())

maior_ab = (A + B + abs(A-B)) / 2
maior_todos = (C + maior_ab + abs(C - maior_ab)) / 2


print(f'{int(maior_todos)} eh o maior')