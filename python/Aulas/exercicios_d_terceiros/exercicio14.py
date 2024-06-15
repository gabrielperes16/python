nome=str(input("Digite seu nome: "))
senha= str(input("Digite sua senha: "))
while senha == nome:
    print("\033[31mErro senha inválida tente novamente!\033[m")
    senha= str(input("Digite sua senha: "))
print("\033[32mSenha Autorizada!\033[m")
