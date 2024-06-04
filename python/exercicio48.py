soma = 0
contador = 0
for numero in range(1,501):
    if numero % 3 == 0:
        if numero % 2:
            contador = contador+1
            soma= soma+numero
print(f"A soma entre todos os {contador} valores é {soma}")
