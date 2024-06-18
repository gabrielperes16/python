num1=int(input("Digite um numero:"))
num2=int(input("Digite outro numero:"))
num3=int(input("Digite mais um numero:"))
num4=int(input("Digite o ultimo  numero:"))
soma=num1,num2,num3,num4
contagem=soma.count(9) 
posicao = soma.index(3)
try:
    posicao_texto = f"O valor 3 apareceu na posição {posicao + 1}"
except ValueError:
    posicao_texto = "O valor 3 não foi encontrado na tupla"
count=0
print(f"Os valores digitados são: {soma}")
print(f"o valor 9 apareceu {contagem} vez")
print(f"O valor 3 apareceu na posição {posicao}")
for n in range(1,5):
    if n %2==0:
        count+=1
print(f"Existem {n} valores Par!")