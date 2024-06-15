from random import randint
velocidade_carro = randint(50,120)
print(velocidade_carro)
km_excedido = velocidade_carro-80
multa= km_excedido*7
if velocidade_carro >= 80:
    print("Você atingiu o limite de velocidade de {} terá de pagar uma multa de {} Reais".format(velocidade_carro,multa))
else:
    print("Não excedeu o limite de velocidade! Esta tudo Bem!")
