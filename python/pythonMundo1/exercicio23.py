valor = int(input("Digite um valor de 0 a 9999: "))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10
print(f"Analisando o numero: {valor}")
print(f"unidade: {u}")
print(f"dezena: {d}")
print(f"centena: {c}")
print(f"milhar: {m}")