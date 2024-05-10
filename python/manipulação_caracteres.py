nome = input("Insira seu nome completo:")
nome_Maiusculo = (nome.upper())
lista= nome.split()
Letras = len(nome)
leitor = len(lista[0])

print("O nome em maiusculo é {}".format(nome_Maiusculo))
print("A quantidade total de Letras com espaços é {}".format(Letras))
print("A quantidade de caracteres no primeiro nome é",leitor)