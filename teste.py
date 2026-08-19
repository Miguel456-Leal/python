import os
os.system("cls")

produto = "celular"
preco = 500
produto_escolha = input("qual e seu produto")
desconto = int(input("qual seria seu desconto:"))
 
if produto_escolha == produto: 
    print(" O Preço do seu Produto é:", preco)

else:   print("não disponivel")

input("Gostaria de que coloque o desconto desejado")
