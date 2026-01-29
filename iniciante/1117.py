lista_notas = []

while True:
    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        lista_notas.append(nota)
        if len(lista_notas) == 2:
            break

print(f"media = {sum(lista_notas)/len(lista_notas):.2f}")
