h_i, h_f = map(int, input().split())
horas = (24 + h_f - h_i) if h_i >= h_f else h_f - h_i
print(f"O JOGO DUROU {int(horas)} HORA(S)")