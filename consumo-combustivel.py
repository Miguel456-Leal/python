import os
os.system("cls")

print("=== Ben Vindo ===")

km = float(input("informe a quilômetragem que você percorreu:"))
com = float(input("informe a quantidade de combustivel gasto:"))

resultado = km / com

consumo = round(resultado,2)

os.system("cls")

print("== informação de dados ==")

print("o valor é de :", consumo)