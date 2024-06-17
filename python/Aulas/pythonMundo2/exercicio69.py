maior_18=masculino=menos_20=0
while True:
    idade=int(input("Idade: "))
    sexo=str(input("M ou F:  ").upper())
    continuar=str(input("Quer continuar? S ou N:  ").upper())
    if sexo == 'M':
        print("Sexo masculino")
        masculino+=1
    if sexo=="F":
        if idade<20:
            menos_20+=1
    if idade>18:
            maior_18+=1
    if continuar == "N":
        break
print(f"\033[32mMaiores de 18 são {maior_18}, do sexo masculino são {masculino} e menores de 20 anos são {menos_20}\033[m")