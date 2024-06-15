while True: 
    nome=str(input("Digite seu nome: "))
    if len(nome) < 3:
        print("Nome inválido caracteres insuficientes!")
        break
    else:
        print("Nome valido!")
    idade=int(input("Digite sua idade: "))
    if idade > 120:
        print("Impossivel pare de mentir!")
    else:
        print("Idade consideravel!")
    salario=float(input("Digite seu salario: "))
    if salario < 0:
        print("Valor inválido!")
    else:
        print("Valor valido!")
    sexo= str(input("Qual o seu sexo? [F] ou [M]").upper())
    if sexo == "M":
        print("Seu sexo é o masculino!")
    else:
        print("Seu sexo é o femenino!")
    print(''' \033[32m
    [ C ] CASADO
    [ S ] SOLTEIRO
    [ V ] VIUVO
    [ D ] DIVORCIADO\033[m''')
    estad_civil=str(input("Qual os seu estado civil? ").upper())
    if estad_civil == "C":
        print("Casado")
    elif estad_civil== 'S':
        print("Solteiro")   
    elif estad_civil== "V":
        print("Viúvo")
    elif estad_civil== "D":
        print("Divorciado")
    print("~"*20)
    print("Informações cadastradas:")
    print(f'''\033[32m
    nome= {nome}
    idade= {idade}
    sexo= {sexo}
    salario= {salario}
    estado civil = {estad_civil}\033[m
''')
    print("~"*20)
    break
print("FIM")
