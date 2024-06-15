
sexo = str(input("Qual o seu sexo?").strip().upper()[0])
while sexo not in "MF":
    sexo=str(input("Mensagem Inválida!").strip().upper()[0])
print(f"Sexo {sexo} registrado!")