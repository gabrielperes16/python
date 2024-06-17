s=cont=num=0
while True:
    num=int(input("Digite um valor[ Digite 999 para parar!]:"))
    if num == 999:
        break
    cont+=1
    s+=num
print(f"Foi digitado {cont} valores e a soma deles é {s}")