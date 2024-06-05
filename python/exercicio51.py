print("=="*20)
print("          10 TERMOS DE UMA PA")
print("=="*20)
primeiro_termo = int(input("Digite o valor do primeiro termo: "))
razão = int(input("Digite o valor da RAZÂO: "))
termos =primeiro_termo+(10-1) *razão
for n in range(primeiro_termo, termos+1, razão):
    print(n, end=" ↦ ")
print("ACABOU!")
