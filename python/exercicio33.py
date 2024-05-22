primeiro= int(input("Digite o valor 1:"))
segundo= int(input("Digite o valor 2:"))
terceiro= int(input("Digite o valor 3:"))
maior = primeiro

if (segundo > maior):
    maior= segundo
if(terceiro > maior):
    maior=terceiro

print("o maior numero é {}".format(maior))
