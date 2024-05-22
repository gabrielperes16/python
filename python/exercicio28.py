from random import randint
valor_aleatorio = randint(0, 1)
print("-=-" *20)
print("Vou pensar em um valor de 0 a 5 tente adivinhar...")
print("-=-" *20)
valor_chutado = input("Qual o valor sorteado? ")

if valor_chutado == valor_aleatorio:
    print("Parabens você acertou!")
else:
    print("Que pena você errou! eu pensei no valor {} e não no {}".format(valor_aleatorio, valor_chutado))
