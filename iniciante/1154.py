lista_idades = []
while (idade := int(input())) >= 0:
    lista_idades.append(idade)

print(f"{sum(lista_idades)/len(lista_idades):.2f}")