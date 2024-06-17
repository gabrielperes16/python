
soma=mais_1000=valor=cont=mais_barato=0
menor=''
while True:
    nome=str(input(f"Digite o nome do produto :  "))
    valor=float(input("Digite o valor deste produto: "))
    cont+=1
    if cont==1:
        mais_barato=valor
        menor=nome
    else:
        if valor<mais_barato:
            mais_barato=valor
            menor=nome

    if valor >=1000:
        mais_1000+=1
    soma+=valor
    continuar=str(input("Quer continuar [ S ] ou [ N ]").upper())
    if continuar=='S':
        print("-="*20)
    else:
        break
print(f"O total gasto é de R${soma:.2f}, no total {mais_1000} custão mais de R$1000 reais")
print(f"O nome do produto mais barato é {nome}")