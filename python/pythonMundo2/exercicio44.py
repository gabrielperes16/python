print("=="*5,"LOJAS PERES","=="*5)
preco_compra= int(input("Preço das Compras: "))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input("Qual é a opção? "))
if escolha == 1:
    print("A sua compra ficou no valor de \033[1;36m{} reais\033[m por conta do Desconto de 10%".format((preco_compra /100)*90))
elif escolha == 2: 
    print("A sua compra ficou no valor de \033[1;36m{} reais\033[m por conta do Desconto de 5%  no cartão".format((preco_compra/100)*95))
elif escolha == 3:

    print("O preço original da compra de \033[1;36m{} reais \033[m foi parcelado em 2x vezes de\033[1;36m {} \033[m e não sofreu alterações!".format(preco_compra,preco_compra/2))
elif escolha ==4:
    parcelas= int(input("Quantas vezes deseja parcelar?"))
    print("A compra foi parcelado em  {} vezes e cada parcela ficou em {:.2f} reais e teve 20%  de juros e ficou no valor de \033[1;36m{} reais\033[m".format(parcelas,(preco_compra/parcelas),(preco_compra/100)*120))
else: 
    print("Metodo de Pagamento \033[1;31m invalido!!! \033[m ")