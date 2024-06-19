compra=''
while True:
    produtos=str(input("digite o nome dos produtos:"))
    preco=float(input("Digite o preco dos produtos:"))
    continuar=str(input("Deseja continuar[ s ] ou [ n ]".lower().strip()))
    if continuar=='n':
        break
    compra+=produtos,preco
print(f'{compra}')

