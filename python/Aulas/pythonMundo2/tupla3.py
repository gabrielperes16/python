from random import randint
num= (randint(1,10)), (randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10))
print(f"Os valores sorteados foram ", end="")
for n in num:
    print(f"{n}",end=" ")
print(f"O maior numero é {max(num)}")
print(f"O menor valor é {min(num)}")
