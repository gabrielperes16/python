cont=0
while True:
    num=int(input("Digite um valor:"))
    if num<=0:
        print("Acabou!")
        break
    for n in range(1,11):
        cont+=1
        tabuada= num*cont
        print(f"A tabuada do {num} x {cont}= {tabuada}")
        
