from random import randint
print("-=" * 12)
print("\033[32mTENTE ADIVINHAR O NÚMERO!\033[m")
print("-=" * 12)
tentativas = 0
computador = randint(0, 4)
Palpite = int(input("Digite um Palpite do Valor: "))
while Palpite != computador:
    tentativas += 1
    print("\033[31mVocê errou! 😢\033[m")
    Palpite = int(input("Digite um Palpite do Valor: "))
tentativas += 1  # Incrementa a tentativa final quando o jogador acerta
print("\033[32mAcertou! 😄\033[m")
print(f"A quantidade de palpites necessária para isto é de \033[32m{tentativas}\033[m tentativas!")
