i = 0.0
j = 1

for cont_i in range(11):
    copia_j = j
    for cont_j in range(3):
        valor_j = copia_j + i
        print(f"I={i:g} J={valor_j:g}")
        copia_j += 1
    i += 0.2
