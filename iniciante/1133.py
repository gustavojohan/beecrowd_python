x = int(input())
y = int(input())

for i in range(x+1, y) if x < y else range(y+1, x):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
