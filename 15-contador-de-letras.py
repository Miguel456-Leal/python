import os
os.system("cls")

palavra = input("escreva sua palavra:")

from collections import Counter

contador = Counter(palavra)

print("sua palavra tem:",contador)
