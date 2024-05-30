variavel= int(input("Digite o primeiro valor: "))
par = variavel % 2
if par == 0:
    print("O valor digitado é {} que é\033[32m PAR \033[me a soma de mais 5 é \033[36m{}\033[m".format(variavel,variavel+5))
else:
    print("O valor digitado é {} que é \033[31m IMPAR\033[m e a soma de mais 8 é \033[36m{}\033[m".format(variavel,variavel+8))