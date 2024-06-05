numero = int(input("Digite um Valor: "))
total= 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[31m', end=" ")
        total+=1
    else:
        print("\033[32m", end=" ")
    print(f"{c}\033[m", end=" ")
print(f"\n O Valor de  {numero} tem a quantidade de {total} de numeros primos! ")
