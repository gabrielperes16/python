print("\033[01;32m=="*11)
print("Sequencia de Fibonacci")
print("=="*11)
n = int(input("\033[36mDigite quantos termos você quer mostrar: "))
t1 = 0
t2 = 1
cont=3
print("\033[32m~\033[m"*30)
while cont<=n:
    cont+=1
    t3= t1+t2
    t4= t3+t2
print(f"\033[01;36m{t1} ↦  {t2}  ↦ {t3}  ↦ {t4}")
