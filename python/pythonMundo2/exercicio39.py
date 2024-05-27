ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade= 2024-ano_nascimento
anos_restantes = 18-idade
ano_alistamento= ano_nascimento+18
print("Quem nasceu me {} tem {} anos em {}".format(ano_nascimento,idade,2024))
if idade >= 18:
    print("Você já deveria ter se alistado há {} anos".format(idade-18))
else:
    print("Ainda Faltam {} anos para o alistamento".format(anos_restantes))
if ano_alistamento < 2024:
    print("Seu alistamento deveria ter acontecido no ano de {}".format(ano_alistamento))
else:
    print("Seu alistamento acontecera no ano de {}".format(ano_alistamento))
