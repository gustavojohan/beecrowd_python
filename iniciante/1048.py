salario = float(input())

if salario >= 0 and salario <= 400:
    p_cento = 15 / 100
    reajuste = p_cento * salario
    salario += reajuste
elif salario > 400 and salario <= 800:
    p_cento = 12 / 100
    reajuste = p_cento * salario
    salario += reajuste
elif salario > 800 and salario <= 1200:
    p_cento = 10 / 100
    reajuste = p_cento * salario
    salario += reajuste
elif salario > 1200 and salario <= 2000:
    p_cento = 7 / 100
    reajuste = p_cento * salario
    salario += reajuste
else:
    p_cento = 4 / 100
    reajuste = p_cento * salario
    salario += reajuste

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {int(p_cento * 100)} %")