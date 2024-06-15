print("\033[32m=="*20)
print("          10 TERMOS DE UMA PA")
print("=="*20, '\033[m')
primeiro_termo = int(input("Digite o valor do primeiro termo: "))
razão = int(input("Digite o valor da RAZÂO: "))
termo = primeiro_termo
contador=1
total=0
add_termos=10
while add_termos !=0:
    total=total+add_termos
    while contador <= total:
        print(f"\033[32m{termo} ↦\033[m", end=" ")
        termo += razão
        contador += 1
    print("PAUSA")
    add_termos = int(input("\033[01;36mQuantos termos a mais você precisa?\033[m"))
print(f"\033[01;36mA quantidade de termos usados foi \033[01;32m{total}\033[m")
print("\033[32mFIM\033[m")
