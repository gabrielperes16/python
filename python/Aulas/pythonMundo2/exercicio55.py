menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f"Peso da pessoa{p}:  "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if p < menor:
            menor = peso
print(f"O maior peso é {maior}Kg")
print(f"O menor peso é {menor}Kg")
