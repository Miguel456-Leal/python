import os
import random
import time

#pyga.me

os.system("cls")

vida_usuario = 100
vida_computador = 100

print(""" 

██████╗░░█████╗░████████╗░█████╗░██╗░░░░░██╗░░██╗░█████╗░  ██████╗░░█████╗░██╗░░██╗███████╗███╗░░░███╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██║░░██║██╔══██╗  ██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░████║██╔══██╗████╗░██║
██████╦╝███████║░░░██║░░░███████║██║░░░░░███████║███████║  ██████╔╝██║░░██║█████═╝░█████╗░░██╔████╔██║██║░░██║██╔██╗██║
██╔══██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██╔══██║██╔══██║  ██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║
██████╦╝██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║░░██║  ██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝
""")

print("=== Escolha seu Pokémon de batalha ===")

print("[1] - Charmander")
print("[2] - Squirtle")
print("[3] - Bulbasaur")
print("[4] - sair")

pokemon_usuario = int(input("Escolha seu pokémon para começar:"))

os.system("cls")
print("Aguarde o Computador Escolher o pokémon")
time.sleep(4)

computador = random.randint(1,3)

while pokemon_usuario == computador:
    computador = random.randint(1,3)

#Exibindo o pokemon do usuario

if(pokemon_usuario == 1):
    print("Você escolheu o Charmander!")
elif(pokemon_usuario == 2):
    print("Você escolheu o Squirtle!")
elif(pokemon_usuario == 3):
    print("Você escolheu o Bulbassaur")

# exibindo o pokémon do computador
if(computador == 1):
    print(" O computador escolheu Charmander!")
elif(computador == 2):
    print("O computador escolheu Squirtle!")
elif(computador == 3):
    print("O computador escolheu Bulbassaur!")

input("pressione <Enter> para iniciar a batalha")

while vida_usuario > 0 or vida_computador >0:
    os.system("cls")

    print(f"vida do Usuário:{vida_usuario}")
    print(f"vida do Computador:{vida_computador}")


    print("== Menu de batalha ==")

    print("[1] - Atacar")
    print("[2] - Usar poção de cura")
    print("[3] - Fugir")

    op_usuario = int(input("Escolha uma opção:"))

    if( op_usuario == 1):
        print("Você atacou!")
        vida_computador -= 10

    elif(op_usuario == 2):
        print(" Você usou cura")
        vida_usuario += 5

    elif(op_usuario == 3):
        print("você saiu da batalha")
        vida_usuario = 0
        time.sleep(2)
        break
        
    time.sleep(3)

    os.system("cls")

    print("Aguarde o Computador")

    time.sleep(3)

    op_computador = random.randint(1,3)

    # verificar a opção escolhida do computador

    if(op_computador == 1):
        print(" o Computador atacou!")
        vida_usuario -=10

    elif(op_computador == 2):
        print("o Computador se curou ")
        vida_computador +=5

    elif(op_computador == 3):
        print(" o Computador Saiu da batalha")
        vida_computador = 0
        time.sleep(2)
        break
    time.sleep(3)
    
#verificar que foi o ganhador

if vida_usuario > vida_computador:
    print("Parabéns você ganhou!")
else:
    print("Gamer Over! o computador venceu!")

print("jogo finalizado")
