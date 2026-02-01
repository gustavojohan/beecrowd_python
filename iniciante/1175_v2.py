def inverte_vetor(vetor):
    inicio = 0
    fim = len(vetor) - 1

    while inicio < fim:
        temp = vetor[inicio]
        vetor[inicio] = vetor[fim]
        vetor[fim] = temp

        inicio += 1
        fim -= 1

    for item in vetor:
        print(item)

vetor = []
for i in range(20):
    vetor.append(int(input()))

inverte_vetor(vetor)