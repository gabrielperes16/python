peso = float(input("Qual o seu peso?  (KG)"))
altura = float(input("Digite a sua Altura: "))
imc = peso / (altura ** 2)
print("O IMC desta pessoa é de {:.1f}".format(imc))
if imc <= 18.5:
    print("Abaixo do Peso!")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
