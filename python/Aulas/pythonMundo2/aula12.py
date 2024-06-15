#Estruturas condicionais aninhadas:
nome = str(input("Digite seu Nome: "))
if nome == "Gabriel":
    print("Que nome bonito!")
elif nome == "Gustavo" or nome == "Lucas":
    print("Que nome mais popular!!!")
else:
    print("Seu nome é bem Normal!")
print("Tenha um bom dia {}{}{} !!!".format('\033[36m', nome, '\033[m'))