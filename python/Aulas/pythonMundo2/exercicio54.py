from datetime import date
ano_atual = date.today().year
jovem=0
idoso=0
for n in range(1,8):
    ano_nascimento=int(input("Digite o seu ano de nascimento: "))
    diferença = ano_atual-ano_nascimento
    if diferença >= 60:
        jovem+=1
    else:
        idoso+=1
    print(f"Em que ano a {n} pessoa nasceu?\033[32m{ano_nascimento}\033[m ")
print(f"A quantidade de Jovens é de \033[32m{jovem}\033[m")
print(f"A quantidade de Idoso é de \033[32m{idoso}\033[m")