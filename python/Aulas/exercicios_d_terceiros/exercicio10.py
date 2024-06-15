num_identificação = int(input("Digite seu numero de identificação: "))
nota1= int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3= int(input("Digite sua terceira nota: "))
media = (nota1+nota2+nota3)/3
media_aproveitamento= (nota1+nota2*2+nota3*3+media)/7
print(f"O numero de identifição deste aluno é {num_identificação}, a sua primeira nota é {nota1} a segunda é {nota2} e a terceira é {nota3}")
print(f"A media dos exercicios é de {media:.2F} pontos, a media de aproveitamento é de {media_aproveitamento:.2f}")
if media_aproveitamento >= 90:
    print("A sua Nota é \033[32mA\033[m")
elif media_aproveitamento >= 75:
    print("A sua nota é \033[32mB\033[m")
elif media_aproveitamento >=60:
    print('A sua Nota é \033[36mC\033[m')
elif media_aproveitamento >= 40:
    print("A sua Nota é \033[31mD\033[m")
