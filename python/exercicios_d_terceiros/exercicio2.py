print("-="*10,)
print("\033[36m  TEMPO DE CASADO \033[m ")
print("-="*10)
nome = str(input("Digite seu nome:"))
print("-="*10)
print('''QUAL O SEU SEXO?
       
[ F ] PARA FEMININO!
[ M ] PARA MASCULINO
      ''')
print("-="*10)
sexo = str(input("Qual o seu sexo? "))
print('''QUAL O SEU ESTADO CIVIL?
       
CASADA OU SOLTEIRA?
      ''')
print("-="*10)
estado_Civil = str(input("Qual o seu Estado Civil? "))

if sexo == "F":
    if estado_Civil == "CASADA":
        tempo_casado=int(input("DIGITE O TEMPO DE CASADA:"))
        print("O seu nome é {} seu sexo é {} seu Estado civil é {} e Você tem {} anos de casada".format(nome,sexo,estado_Civil,tempo_casado))
    else:
        print("\033[31mMais nenhuma informação é nescessaria!\033[m")
    
