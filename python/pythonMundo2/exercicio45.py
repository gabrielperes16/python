import time
from random import randint

print('''suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

Lista = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
jogador = int(input("Qual a sua jogada? "))

print("-="*11)
print("     JO", "KEN", "PO!!!     ")
print("O computador escolheu {}".format(Lista[computador]))
print("O jogador escolheu {}".format(Lista[jogador]))
print("-="*11)

if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("O jogador Venceu!")
    elif jogador == 2:
        print("O computador Venceu!")
elif computador == 1:
        if jogador == 0:
            print("O computador Venceu!")
        elif jogador == 1:
            print("EMPATE!")
        elif jogador == 2:
            print("O jogador VENCEU!")
elif computador == 2:
    if jogador == 0:
        print("O jogador VENCEU")
    elif jogador == 1:
        print("O computador VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
else:
    print("JOGADA INVALIDA")
