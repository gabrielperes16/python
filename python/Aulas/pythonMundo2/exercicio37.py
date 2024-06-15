numero1=  int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases de Conversão:
[ 1 ] converter para BINÁRIO:
[ 2 ] converter para OCTAL:
[ 3 ] converter para HEXADECIMAL:''')
escolha= int(input("Sua opção:"))
if escolha == 1:
    print("{} Convertido para BINÁRIO é igual a {}".format(numero1, bin(numero1)[2:]))
elif escolha == 2 :
    print("{} convertido para OCTAL é igual a {}".format(numero1, oct(numero1)[2:]))
elif escolha == 3 :
    print("{} convertido em HEXADECIMAL é igual a {}".format(numero1,hex(numero1)[2:]))
else:
    print("\033[36m Valor invalido! \033[m ")
