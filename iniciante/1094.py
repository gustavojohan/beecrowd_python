qnt_testes = int(input())

cobaias = {"Total": 0, "C": 0, "R": 0, "S": 0}

for i in range(qnt_testes):
    qnt_cobaias, tipo_cobaia = input().split()
    qnt_cobaias = int(qnt_cobaias)
    cobaias[tipo_cobaia] += qnt_cobaias
    cobaias["Total"] += qnt_cobaias

print(f"Total: {cobaias["Total"]} cobaias")
print("Total de coelhos: ", cobaias["C"])
print("Total de ratos: ", cobaias["R"])
print("Total de sapos: ", cobaias["S"])
print(f"Percentual de coelhos: {cobaias['C']/cobaias["Total"]:.2f} %")
print(f"Percentual de ratos: {cobaias['R']/cobaias["Total"]:.2f} %")
print(f"Percentual de sapos: {cobaias['S']/cobaias["Total"]:.2f} %")