while True:
    lista_notas = []
    finaliza_calculo = False

    while True:
        nota = float(input())

        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            lista_notas.append(nota)
            if len(lista_notas) == 2:
                break

    print(f"media = {sum(lista_notas)/len(lista_notas):.2f}")
    while True:
        novo_calculo = input("novo calculo (1-sim 2-nao)\n")
        if novo_calculo == '1':
            break
        elif novo_calculo != '1' and novo_calculo != '2':
            continue
        else:
            finaliza_calculo = True
            break
    
    if finaliza_calculo:
        break