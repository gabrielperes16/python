nome = str(input("Digite seu nome: "))
cores = {
    "limpa": "\033[m",
    "azul": "\033[36m"
}
print("prazer em te conhecer {}{}{}!!!".format(cores['azul'], nome, cores['limpa']))
