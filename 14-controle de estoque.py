import os
os.system("cls")

print("== Estoque ==")

produto = float(input("informe a quantidade do produto:"))

if produto >=5:
    print("ok")
else:
    print("baixo estoque")