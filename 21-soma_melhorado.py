import os
os.system("cls")

#passo 1 entradas de dados
print("seja bem-vindo a super calculadora")

resposta = "sim"

while resposta =="sim":
    valor01 = float(input("informe o primeiro valor:"))
    valor02 = float(input("informe outro valor:"))

#Passo 2 processamento

    total = valor01 + valor02

 #passo 3 saida

    print(f"A soma é:{total}")   
    resposta = input("digite Sim para executar novamente:")
    os.system("cls")
input("pressione <Enter> para encerrar..")