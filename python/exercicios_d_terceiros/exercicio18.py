print('''   \033[32m
[ 1 ] EM PILHA
[ 2 ] EM FILA
 \033[m     ''')
escolha =int(input("Seu Escolha: "))
if escolha == 1:
    for n in range(1,21):
        print(n)
elif escolha ==2:
    for n in range(1,21):
        print(f"{n}",end=", ")
else:
    print("ERRO!")