primeiro= int(input("Digite o valor 1:"))
segundo= int(input("Digite o valor 2:"))
terceiro= int(input("Digite o valor 3:"))
maior = primeiro
menor = primeiro
if (segundo > maior):
    maior= segundo
if(terceiro > maior):
    maior=terceiro
if segundo < menor:
    segundo=menor
if terceiro < menor:
    terceiro=menor
print("o maior numero é {}".format(maior))
print("O menor numero é {}".format(menor))
