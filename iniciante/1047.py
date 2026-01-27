h_i, m_i, h_f, m_f = map(int, input().split())

inicio_minutos = h_i * 60 + m_i
fim_minutos = h_f * 60 + m_f

if fim_minutos > inicio_minutos:
    duracao = fim_minutos - inicio_minutos
elif fim_minutos < inicio_minutos:
    duracao = (fim_minutos + 24*60) - inicio_minutos
elif fim_minutos == inicio_minutos:
    duracao = 24*60

horas = duracao / 60
minutos = duracao % 60

print(f"O JOGO DUROU {int(horas)} HORA(S) E {minutos} MINUTO(S)")