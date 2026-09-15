import os
os.system("cls")

print("== tabuada ==")

numero = int(input("informe um numero inteiro:"))

contador = 0

while contador <= 10:
    print(f"{numero} X {contador} = {numero * contador}")
    contador+=1


input("pressione <Enter> para encerrar..")