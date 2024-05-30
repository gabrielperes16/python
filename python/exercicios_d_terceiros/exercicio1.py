A= int(input("Digite um Valor:"))
B = int(input("Digite o segundo Valor:"))
C= int(input("Digite o terceiro Valor: "))
soma= A+B
if soma < C:
    print("A soma de {} e {} é menor que {}".format(A,B,C))
else:
    print("A soma de {} e {} é maior que {}".format(A,B,C))