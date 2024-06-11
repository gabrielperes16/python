print("\033[32m=="*20)
print("          10 TERMOS DE UMA PA")
print("=="*20,'\033[m')
primeiro_termo = int(input("Digite o valor do primeiro termo: "))
razão = int(input("Digite o valor da RAZÂO: "))
termo= primeiro_termo
contador=1
while contador <= 10:
    print(f"\033[32m{termo} ↦\033[m", end=" ")
    termo+= razão
    contador+=1
print("\033[01;36mFIM\033[m")
