lista = []
cont_pares = 0
cont_impares = 0
cont_posi = 0
cont_neg = 0

for i in range(5):
    lista.append(float(input()))

for numero in lista:
    if numero % 2 == 0:
        cont_pares += 1
        if numero < 0:
            cont_neg += 1
        elif numero > 0:
            cont_posi += 1
    else:
        cont_impares += 1
        if numero < 0:
            cont_neg += 1
        elif numero > 0:
            cont_posi += 1

print(f"{cont_pares} valor(es) par(es)\n" +
      f"{cont_impares} valor(es) impar(es)\n" +
      f"{cont_posi} valor(es) positivo(s)\n" +
      f"{cont_neg} valor(es) negativo(s)")

