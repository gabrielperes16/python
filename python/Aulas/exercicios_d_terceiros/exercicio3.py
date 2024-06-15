valor= int(input("Digite um valor Qualquer: "))
par= valor % 2
if par == 0:
    print("Este valor é \033[32mPAR!\033[m")
else:
    print("Este valor é \033[31mIMPAR!\033[m")