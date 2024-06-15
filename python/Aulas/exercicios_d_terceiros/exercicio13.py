nota= int(input("Digite sua nota entre 0 a 10: "))
while nota > 10:
    print("\033[31mEste valor é invalido!\033[m")
    nota= int(input("Digite sua nota entre 0 a 10: "))
print(f"\033[32mEste é um valor valido de {nota} pontos\033[m")