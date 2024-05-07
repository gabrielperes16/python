# co= float(input("Digite o comprimento do cateto oposto:"))
# ca = float(input("Digite o comprimento do catetto adjacente:"))
# hi= (co**2 + ca**2)**(1/2)
# print("A hipotenusa vai medir {:.2f}".format(hi))

# from math import hypot
# co = float(input("Digite o comprimento do cateto oposto"))
# ca = float(input("Digite o comprimento do cateto adjacente"))
# hi = hypot(co, ca)
# print("A hiponusa vai medir {:.2f}".format(hi))



import math
an = float(input("Digite o valor do angulo que voce deseja="))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print('O angulo de {} tem o seno de {:.2f}'.format(an,seno))
print("O angulo de {} tem o cosseno de {:.2f}".format(an,cosseno))
print("O angulo de {} tem o tangente de {:.2f}".format(an,tangente))