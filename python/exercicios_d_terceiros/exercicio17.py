cont = 0
pais_a = int(input("Digite a quantidade populacional deste pais: "))
pais_b = int(input("Digite a quantidade populacional do pais B: "))
taxa_a=float(input("digite a taxa: "))
taxa_b=float(input("Digite a taxa: "))
while pais_a <= pais_b:
    pais_a+= (pais_a/100)*taxa_a
    pais_b+= (pais_b/100)*taxa_b
    cont += 1

print(f'Foi nescessario {cont} anos para o pais A ultrapaçar o pais B com {pais_a:.2f}')
