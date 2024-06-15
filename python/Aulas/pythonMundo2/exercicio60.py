f=1
num = int(input("Digite um numero para calcular o Fatorial: "))
c= num
print(f"O fatorial de {num}!= ", end="")
while c>  0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")
