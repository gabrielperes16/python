soma=0
cont=0
for n in range(1,7):
    numero=int(input(f"Digite o valor {n}: "))
    if numero % 2 == 0:
       cont+= 1
       soma+=numero
print(f"Você informou {cont} numeros e a soma foi {soma}")