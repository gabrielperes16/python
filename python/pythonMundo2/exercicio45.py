from random import randint
from time import sleep
print('''suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ("Pedra","Papel","Tesoura")
computador = randint(0, 2)
jogador = int(input("Qual a sua jogada? "))
print("-="*11)
print("jo")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA')
else:
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
print("-="*11)
if computador == 0:
    if computador == jogador:
     print('EMPATE')
    elif jogador == 1:
        print("O jogador Venceu!")
    elif jogador == 2:
        print("O computador Venceu!")
    else:
        print("JOGADA INVALIDA!!!")
elif computador == 1:
        if jogador == 0:
            print("O computador Venceu!")
        elif jogador == 2:
            print("O jogador VENCEU!")
elif computador == 2:
    if jogador == 0:
        print("O jogador VENCEU")
    elif jogador == 1:
        print("O computador VENCEU!")

