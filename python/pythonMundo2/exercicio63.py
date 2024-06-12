print("\033[01;32m=="*11)
print("Sequencia de Fibonacci")
print("=="*11)
n = int(input("\033[36mDigite quantos termos você quer mostrar: "))
t1=0
t2=1
print(f"{t1} , {t2} ,", end=" ")
cont= 3
while cont<= n:
    t3= t1+t2
    t1=t2
    t2=t3
    cont+=1
    print(f"{t3} , ", end=" ")
print("FIM")