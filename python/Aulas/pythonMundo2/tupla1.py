import num2words
num = int(input("Digite um valor entre 0 e 20: "))
if num > 20 or num <0:
    print("Erro!,tente novamente")
else:
    num_ptbr=num2words.num2words(num, lang='pt-br')
    print(num_ptbr)

