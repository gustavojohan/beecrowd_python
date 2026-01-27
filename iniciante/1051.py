renda = float(input())
imposto = 0

if renda > 2000:
    tributavel = renda - 2000
    if tributavel > 2500:
        imposto += 1000*0.08 + 1500*0.18 + (tributavel - 2500)*0.28

    elif tributavel > 1000 and tributavel <= 2500:
        imposto += 1000*0.08 + (tributavel - 1000)*0.18
    else:
        imposto += tributavel*0.08
    
    print(f"R$ {imposto:.2f}")
else:
    print("Isento")