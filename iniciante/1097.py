i = 1
j = 7

for cont_i in range(5):
    copia_j = j
    for cont_j in range(3):
        print(f"I={i} J={copia_j}")
        copia_j-= 1
    i+=2
    j+=2