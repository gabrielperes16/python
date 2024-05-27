import sys
print('-=-'*20)
print('''
        Caso seu sexo seja MASCULINO tecle: [1]
        Caso seu sexo seja FEMININO tecle:  [2]\n''')
print('-=-'*20)

sexo= int(input("Qual o seu sexo? "))
if sexo == 1:
    print("O sexo escolhido é o MASCULINO!!!")
elif sexo == 2:
    print("O sexo escolhido é o FEMININO!!!")
else:
    print("Valor inválido!!!")

if sexo == 1:
    print("O sexo masculino pode se alistar!!!")
elif sexo == 2:
    print("O sexo feminino não pode se alistar!!!")
    sys.exit(0)
else:
    print("Valor inválido!!!")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2024-ano_nascimento
anos_restantes = 18-idade
ano_alistamento = ano_nascimento+18
print("Quem nasceu me {} tem {} anos em {}".format(ano_nascimento, idade, 2024))
if idade >= 18:
    print("Você já deveria ter se alistado há {} anos".format(idade-18))
else:
    print("Ainda Faltam {} anos para o alistamento".format(anos_restantes))
if ano_alistamento < 2024:
    print("Seu alistamento deveria ter acontecido no ano de {}".format(ano_alistamento))
else:
    print("Seu alistamento acontecera no ano de {}".format(ano_alistamento))
