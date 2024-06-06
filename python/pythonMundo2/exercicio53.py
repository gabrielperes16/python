frase= str(input("Digite uma frase: ").strip().upper())
palavras=frase.split()
junto="".join(palavras)
inverso=junto[::-1]
print(junto,inverso)
if inverso == junto:
    print("Temos um Palindromo!")
else:
    print("Isto não é um Palindromo!")