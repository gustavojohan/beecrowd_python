t = int(input())

hours = t // 3600
minutes = (t % 3600) // 60
sec = (t % 3600) % 60

print(f'{hours}:{minutes}:{sec}')