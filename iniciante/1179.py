impar = []
par = []

for i_input in range(15):
    valor = int(input())
    if valor % 2 == 0:
        par.append(valor)
        if len(par) == 5:
            for i_par in range(5):
                print(f"par[{i_par}] = {par[i_par]}")
            par = []
    else:
        impar.append(valor)
        if len(impar) == 5:
            for i_impar in range(5):
                print(f"impar[{i_impar}] = {impar[i_impar]}")
            impar = []

for i, valor in enumerate(impar):
    print(f"impar[{i}] = {valor}")

for i, valor in enumerate(par):
    print(f"par[{i}] = {valor}")