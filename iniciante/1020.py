age = int(input())

years = age // 365
months = (age % 365) // 30
days = (age % 365) % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')