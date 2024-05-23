reta1 = float(input("Digite o Valor da primeira reta: "))
reta2 = float(input("Digite o Valor da segunda reta: "))
reta3 = float(input("Digite o Valro da terceira reta: "))
if reta1< reta2 + reta3 and reta2< reta1+reta3 and reta3 < reta2+reta1:
    print("Este segmento pode formar um triangulo!")
else:
    print("Este segmento não pode formar um triangulo!")