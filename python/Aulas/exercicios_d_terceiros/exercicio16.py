cont = 0
pais_a = 80000
pais_b = 200000
calculo_a = (pais_a/100)*103
calculo_b= (pais_b/100)*101.5
while pais_a < pais_b:
    calculo_a = (pais_a/100)*103
    calculo_b= (pais_b/100)*101.5
    pais_a=calculo_a
    pais_b=calculo_b
    cont += 1

print(f'Foi nescessario {cont} anos para o pais A ultrapaçar o pais B com {calculo_a:.2f}')
