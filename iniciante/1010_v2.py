cd_p1, n_p1, v_p1 = map(str, input().split())
cd_p1, n_p1 = map(int, (cd_p1, n_p1))
v_p1 = float(v_p1)

cd_p2, n_p2, v_p2 = map(str, input().split())
cd_p2, n_p2 = map(int, (cd_p2, n_p2))
v_p2 = float(v_p2)

print(f'VALOR A PAGAR: R$ {((n_p1*v_p1) + (n_p2*v_p2)):.2f}')