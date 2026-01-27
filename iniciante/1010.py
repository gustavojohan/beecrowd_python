"""
map(lambda x: int(x) if x.isdigit() else float(x), input().split())
    map(funcao, lista) → Aplica a função fornecida a cada elemento da lista.
    lambda x: int(x) if x.isdigit() else float(x) → Função anônima (lambda) que decide como converter cada elemento.


"""

cd_p1, n_p1, v_p1 = map(lambda x: int(x) if x.isdigit() else float(x), input().split())
cd_p2, n_p2, v_p2 = map(lambda x: int(x) if x.isdigit() else float(x), input().split())

print(f'VALOR A PAGAR: R$ {((n_p1*v_p1) + (n_p2*v_p2)):.2f}')
