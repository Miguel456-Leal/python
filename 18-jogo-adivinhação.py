import os
os.system("cls")

print("== jogo de adivinhação ==")

palpite= int(input("fale um número de 1 a 10:"))

import random

numero =random.randint(1,10)

if palpite == numero:
    print("Você Acerto")
elif palpite < numero:
    print("Errou o número é maior")
elif palpite > numero:
    print("Errou o número e menor")