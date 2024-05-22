numero = int(input("Digite um valor qualquer: "))
resto = numero % 2

if resto == 0:
    print("O número digitado {} é par".format(numero))
else:
    print("O número digitado {} é ímpar".format(numero))
