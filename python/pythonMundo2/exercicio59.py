from time import sleep
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor2: "))
print("-="*15)
print('''\033[01;32m    [ 1 ] SOMA
    [ 2 ] SUBTRAÇÃO
    [ 3 ] MULTIPLICAÇÃO
    [ 4 ] DIVISÃO
    [ 5 ] MAIOR OU MENOR
    [ 6 ] NOVOS NUMEROS
    [ 7 ] SAIR DO PROGRAMA\033[m''')
print("-="*15)
escolha = int(input("Qual sua escolha?"))
if escolha == 1:
    soma = valor1+valor2
    print(f"A soma dos valores é \033[01;32m{soma}\033[m")
elif escolha==2:
    subtracao= valor1-valor2
    print(f"A subtração de {valor1} por {valor2} é \033[01;32m{subtracao}\033[m")
elif escolha == 3:
    multiplicacao = valor1*valor2
    print(f"A multiplicação dos valores é \033[01;32m{multiplicacao}\033[m")
elif escolha== 4:
    divisão = valor1/valor2
    print(f"A divisão de {valor1} dividido por {valor2} é igual a \033[01;32m{divisão:.2f}\033[m")
elif escolha == 5:
    menor = valor2
    maior = valor1
    if maior > valor2:
        print(f"O valor \033[01;32m{valor1}\033[m é maior e o valor \033[01;32m{menor}\033[m é o menor!")
    elif maior < valor2:
        menor=valor1
        print(f"O valor \033[01;32m{valor2}\033[m é maior e o valor \033[01;32m{menor}\033[m é o menor!")
    elif maior== valor2:
        print("\033[01;36mOS valores são identicos!\033[m")
elif escolha == 6:
    print("\033[36m DIGITE NOVOS VALORES: \033[m")
    valor1 = int(input("Digite o valor 1: "))
    valor2 = int(input("Digite o valor2: "))
elif escolha == 7:
    print("\033[01;32mFinalizando....\033[m")
    sleep(1.5)
    print("\033[01;32mPrograma finalizado. Tente novamente!\033[m")
else:
    print("\033[01;31mResposta Inválida! tente novamente!\033[m")
