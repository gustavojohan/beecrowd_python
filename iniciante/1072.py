qnt_leituras = int(input())
lista_valores = []

for i in range(qnt_leituras):
    lista_valores.append(int(input()))

cont_dentro = 0
cont_fora = 0

for valor in lista_valores:
    if valor >= 10 and valor <= 20:
        cont_dentro += 1
    else:
        cont_fora += 1

print(f"{cont_dentro} in")
print(f"{cont_fora} out")