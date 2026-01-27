x = int(input())
x_50 = (x % 100)
x_20 = x_50 % 50
x_10 = x_20 % 20
x_5 = x_10 % 10
x_2 = x_5 % 5
x_1 = x_2 % 2

print(x)
print(f'{int(x//100)} nota(s) de R$ 100,00')
print(f'{int(x_50//50)} nota(s) de R$ 50,00')
print(f'{int(x_20//20)} nota(s) de R$ 20,00')
print(f'{int(x_10//10)} nota(s) de R$ 10,00')
print(f'{int(x_5//5)} nota(s) de R$ 5,00')
print(f'{int(x_2//2)} nota(s) de R$ 2,00')
print(f'{int(x_1)} nota(s) de R$ 1,00')