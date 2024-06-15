a = int(input("Digite o valor 1: "))
b = int(input("Digite o valor 2:"))
if a == b:
    resultado= a+b
elif a != b:
    resultado= a*b
c = resultado
print("O primeiro Valor é \033[36m{}\033[m e o segundo é \033[36m{}\033[m gerando o Valor da variavel C que é \033[32m{}\033[m".format(a,b,resultado))