peso = int(input("Digite seu peso(KG): "))
altura = int(input("Digite sua altura(CM): "))
imc =peso/(altura*altura)
if imc <= 18.5:
    print(f"O seu IMC é {imc:.4f} você esta abaixo do peso!")
elif imc <= 25:
    print(f"O seu IMC de {imc:.4f} esta no peso normal!")
elif imc <=30:
    print(f"O seu IMC de {imc:.4f} esta acima do peso!")
else:
    print(f"O seu IMC é de {imc:.4f} você esta obeso!")