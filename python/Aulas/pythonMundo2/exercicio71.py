valor=int(input("Digite o valor: "))
total=valor
ced=50
ced2=20
ced3=10
ced4=1
total_ced=total_ced2=total_ced3=total_ced3=total_ced4=0
while True:
    if total >= ced:
        total-= ced
        total_ced+=1
    if total >= ced2:
        total-=ced2
        total_ced2+=1
    if total >= ced3:
        total -= ced3
        total_ced3+=1
    if total >= ced4:
        total-=ced4
        total_ced4+=1
        if total==0:
            break
print(f"Foi nescessario {total_ced} de CINQUENTA reais {total_ced2} de VINTE {total_ced3} de DEZ e {total_ced4} de UM")

