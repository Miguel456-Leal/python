import os
os.system("cls")

user = input("coloque o nome do usuário:")
senha = int(input("informe a sua senha:"))

if user == "miguel" and senha == 123:
    print("acesso liberado")
else:
    print("acesso negado")