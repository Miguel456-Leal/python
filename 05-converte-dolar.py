import os 
os.system("cls")

print("=== convetor de dolar ===")

input("deseja saber quanto vale o dolar?:")
print("O valor do dolar e R$5,17")

dolar = float(input("informe o valor para conveter:"))

Real = dolar * 5.17
Resultado = round(Real, 2)

input("pressione <Enter> para continuar..")
import os 
os.system("cls")

print("=== relatorio da covertencia ===")

print("O valor inserido em dolar é:",dolar)
print("O valor em Reais é:",Resultado)
