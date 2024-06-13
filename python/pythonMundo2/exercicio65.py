cont=1
continuar="S"
soma=media=cont=maior=menor=0

while continuar != "n":
    num=int(input("Digite um número: ").upper())
    soma+=num
    cont+=1
    if cont==1:
        maior=menor=cont
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num

    continuar=str(input("Quer continuar? [S/N]"))
media=soma/cont
print(f"\033[32mVocê digitou {cont} números e a média é de {media:.2f}\033[m")
print(f"\033[32mO valor maior é {maior} e o menor é {menor}\033[m")
