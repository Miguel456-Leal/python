import os
os.system("cls")

print("== calculadora de estudo ==")

valor = float(input("informe as horas estudadas:"))

if valor < 3:
    print("pouco tempo de estudo")
elif valor <= 4:
    print("bom")
else:
    print("muito estudo")
