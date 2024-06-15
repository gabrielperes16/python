idade=0
soma_idade=0
mais_velho=0
nomevelho= ""
totmulher20= 0
for p in range(1,3):
    print(f"----{p}º PESSOA----")
    nome=str(input("Qual o seu nome? ").upper)
    idade=int(input("Qual a sua idade? "))
    sexo=str(input("Qual o seu sexo [ M/F ]: "))
    soma_idade+= idade
    if p== 1 and sexo == "Mm":
        mais_velho= idade
        nomevelho= nome
    if sexo in "Mm" and idade > mais_velho:
            mais_velho= idade
            nomevelho=nome
    if sexo in "Ff" and idade < 20:
            totmulher20+=1
mediaidade= soma_idade/4
print(f"A media de idade do grupo é de {mediaidade}")
print(f"O homem mais velho do grupo é de {mais_velho}")
print(f"Tem {totmulher20} mulheres com mais de 20 anos!")
