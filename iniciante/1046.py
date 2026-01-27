h_i, h_f = map(int, input().split())

if h_i > h_f:
    duracao = (12 + h_f) - (h_i - 12)
    print(f'O JOGO DUROU {duracao} HORA(S)')
elif h_i == h_f:
    print('O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {h_f - h_i} HORA(S)')