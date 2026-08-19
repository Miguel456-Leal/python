import os
os.system("cls")

#Passo 01 entrada
print("Bem vindo a calculadora de desconto")

produto = input("informe o nome do produto de sua preferencia :")
preco = float(input("qual seria o preço do produto:"))
desconto = float(input("desconto do vale:"))

#Passo 02 processamento
total = preco * desconto / 100

total2 = preco - total

#Passo 03 saida
input("pressione <Enter> para visualizar..")
os.system("cls")

print("=== Relatorio Final ===")
print("produto", produto)
print("preço original",preco)
print("desconto",desconto)
print("O valor do produto é:", total2)

input("pressione <Enter> para encerrar")
