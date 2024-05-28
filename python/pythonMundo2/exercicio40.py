nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
media = (nota1+nota2)/2
print("O aluno 1 tirou {} e o aluno 2 tirou {} portanto a média dos 2 é {}".format(
    nota1, nota2, media))
if 7 > media >= 5.0:
    print("A nota {} é abaixo da média nescessaria, Você esta de reprovado!!!".format(media))
elif media <= 6.9:
    print("A nota {} é abaixo da média nescessaria, Você esta de recuperação!!!".format(media))
else:
    print("A nota {} é acima da média nescessaria, Você passou parabéns!!!".format(media))
