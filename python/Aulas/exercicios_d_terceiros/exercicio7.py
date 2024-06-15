valor1 = int(input("Digite o valor1: "))
valor2 = int(input("Digite o valor2: "))
valor3 = int(input("Digite o valor3: "))
if valor1 > valor2 and valor1 > valor3:
    valor2 > valor3
    print(f"primeiro {valor1} segundo {valor2} terceiro {valor3}")
elif valor2 > valor1 and valor2> valor3:
    valor3 > valor1
    print(f"primeiro {valor2}  segundo {valor1} terceiro {valor2}")
elif valor3 > valor1 and valor3> valor2:
    valor2> valor1
    print(f"primeiro {valor3}  segundo {valor2} terceiro {valor1}")

