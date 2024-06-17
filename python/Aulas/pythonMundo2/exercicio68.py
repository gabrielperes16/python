import random
while True:
    pc=random.randint(1,501)
    num=int(input("Digite um valor: "))
    escolhas=('PAR','IMPAR')
    jogador=str(input("[ PAR ]  ou  [ IMPAR ]: ").upper())
    escolha_pc=random.choice(escolhas)
    print(f"A sua escolha foi {jogador} e a do PC foi {escolha_pc}")
    if jogador == escolha_pc:
        print("erro! Tente Novamente!")
        break
    calculo=(pc+num)%2
    print(f"O seu valor digitado foi {num} e a do PC foi {pc} o resultado do calculo é {calculo}")
    if calculo==1:
        print("IMPAR ganhou!")
    else:
        print("PAR ganhou!")
        break

