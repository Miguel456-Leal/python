import os
os.system("cls")

ano = int(input("fale o ano que está:"))

ano1 = 0
anobissexto = ano % 4

if anobissexto == ano1:
    print("esse ano e bissexto")
else:
    print("não e bissexto")