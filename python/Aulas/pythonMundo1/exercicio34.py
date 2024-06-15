salario= int(input("Digite seu salario? "))
if salario <= 1250:
    novo = (salario/100)*110
else:
    novo = (salario/100)*115
print("O seu salario novo será {}".format(novo))