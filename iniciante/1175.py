vetor = []
for i in range(20):
    vetor.append(int(input()))

for index, item in enumerate(reversed(vetor)):
    print(f"N[{index}] = {item}")