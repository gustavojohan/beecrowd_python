n = float(input())

#NOTAS
n_50 = (n % 100)
n_20 = n_50 % 50
n_10 = n_20 % 20
n_5 = n_10 % 10
n_2 = n_5 % 5

#MOEDAS
m_1 = n_2 % 2
m_50 = m_1 % 1
m_25 = m_50 % 0.50
m_10 = m_25 % 0.25
m_05 = m_10 % 0.10
m_01 = m_05 % 0.05

print('NOTAS:')
print(f'{int(n//100)} nota(s) de R$ 100.00')
print(f'{int(n_50//50)} nota(s) de R$ 50.00')
print(f'{int(n_20//20)} nota(s) de R$ 20.00')
print(f'{int(n_10//10)} nota(s) de R$ 10.00')
print(f'{int(n_5//5)} nota(s) de R$ 5.00')
print(f'{int(n_2//2)} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{int(m_1)} moeda(s) de R$ 1.00')
print(f'{int(m_50 // 0.50)} moeda(s) de R$ 0.50')
print(f'{int(m_25 // 0.25)} moeda(s) de R$ 0.25')
print(f'{int(m_10 // 0.10)} moeda(s) de R$ 0.10')
print(f'{int(m_05 // 0.05)} moeda(s) de R$ 0.05')
print(f'{round(m_01/0.01)} moeda(s) de R$ 0.01')