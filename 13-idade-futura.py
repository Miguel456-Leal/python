import os
os.system("cls")

idade = int(input("informe sua idade:"))

from datetime import date

idade1 = date.today().year - idade

resultado = 2035 - idade1

print("sua idade futura é:",resultado)