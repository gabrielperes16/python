valor_casa = int(input("Digite o Valor da casa: "))
Salario = int(input("Digite o seu salario: "))
Anos= int(input("Digite em quantos anos você vai pagar: "))
mensalidade = valor_casa / (Anos*12)

if mensalidade >= (Salario/100)*30:
    print("infelizmente a prestação de \033[1;36m{:.2f}\033[m  excedeu os 30%  do seu salario de {} reais".format(mensalidade,Salario))
else:
    print("Parabéns o emprestimo foi realizado com \033[1;36m sucesso!!! \33[m")