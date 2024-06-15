nota1 = float(input("Digite sua nota:"))
nota2 = float(input("Digite sua segunda nota:"))
media= (nota1 + nota2) / 2
print("A media de suas notas são {}".format(media))
if media >= 6.0:
    print("Voce atingiu a media. Parabéns!")
else:
    print("Voce não atingiu a média. Estude mais!")