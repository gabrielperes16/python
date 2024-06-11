repetiçoes=0
print("=="*20)
print("          10 TERMOS DE UMA PA")
print("=="*20)
n=0
primeiro_termo = int(input("Digite o valor do primeiro termo: "))
razão = int(input("Digite o valor da RAZÂO: "))
while repetiçoes==10:
    termos =primeiro_termo+(10-1) *razão
    n=primeiro_termo+ (termos+1)*razão
repetiçoes+=1
print(f"A PA do valor {primeiro_termo} e o valor da razão {razão} é igual a {n}", end=" ↦ ")
print("ACABOU!")
