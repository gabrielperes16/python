num1 = int(input("Digite o primeiro Valor:"))
num2 = int(input("Digite o segundo Valor:"))
if num1 > num2:
    print("O valor {} é maior que o Valor {}".format(num1,num2))
elif num2 > num1:
    print("O valor {} é maior que o Valor {}".format(num2,num1))
else:
    print("Os valores são identicos!!!")