#  Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
num = int(input("Digite um Valor: "))
for n in range(11):
    print(f"{num} x {n} = {num*n}")