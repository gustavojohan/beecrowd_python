senha_correta = 2002

while True:
    senha_digitada = int(input())
    if senha_digitada != senha_correta:
        print("Senha Invalida")
    else:
        print("Acesso Permitido")
        break