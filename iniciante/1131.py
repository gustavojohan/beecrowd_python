vitorias_inter = 0
vitorias_gremio = 0
empates = 0
partidas = 0

while True:
    finaliza_grenal = False
    inter, gremio = map(int, input().split())
    partidas += 1

    if inter > gremio:
        vitorias_inter += 1
    elif gremio > inter:
        vitorias_gremio += 1
    else:
        empates += 1

    while True:
        novo_grenal = input("Novo grenal (1-sim 2-nao)\n")
        if novo_grenal == '1':
            break
        else:
            finaliza_grenal = True
            break
    
    if finaliza_grenal:
        print(f"{partidas} grenais")
        print(f"Inter:{vitorias_inter}")
        print(f"Gremio:{vitorias_gremio}")
        print(f"Empates:{empates}")
        if inter > gremio:
            print("Inter venceu mais")
        elif gremio > inter:
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")
        break