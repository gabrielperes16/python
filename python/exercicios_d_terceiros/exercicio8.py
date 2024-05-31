print("-="*10)
print("\033[36mCALCULADORA DE PESO\033[m")
print("-="*10)
print("-="*10)
print('''QUAL O SEU SEXO?
[ F ] PARA FEMENINO
[ M ] PARA MASCULINO''')
print("-="*10)
sexo = str(input("Digite qual o seu Sexo: "))
altura= float(input("Digite qual a sua altura(cm): "))
peso= int(input("Quantos kilos você pesa? "))
if sexo =='M':
    peso_ideal= (altura/100*72)-58
    if peso_ideal > peso:
        print(f"Cuidado Você esta abaixo do peso ideal de {peso_ideal} Kilos!")
    elif peso_ideal < peso:
        print(f"Cuidado você esta acima do peso ideal! de {peso_ideal} Kilos!!")
if sexo == "F":
    peso_ideal=  (62.1 *(altura/100))-44.7
    if peso_ideal> peso:
        print(f"Cuidado você esta abaixo do peso ideal de {peso_ideal}")
    elif peso_ideal< peso:
        print(f"Cuidado você esta acima do peso ideal de {peso_ideal}")
