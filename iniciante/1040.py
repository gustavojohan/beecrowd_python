n1, n2, n3, n4 = map(float, input().split())

p1 = 2
p2 = 3
p3 = 4
p4 = 1

media = ((n1*p1) + (n2*p2) + (n3*p3) + (n4*p4)) / (p1+p2+p3+p4)

print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n_exame = float(input())
    print(f'Nota do exame: {n_exame:.1f}')
    media_final = (media + n_exame) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')