cont=0
numero= int(input("\033[36mDigite um valor[999] para parar: \033[m"))
soma=numero
while numero != 999:
    numero= int(input("\033[36mDigite um valor[999] para parar: \033[m"))
    cont+=1
soma=numero+numero
print(f"A soma total dos valores é {soma}")
print(f"\033[32mA quantidade de valores inseridos é {cont}\033[m")