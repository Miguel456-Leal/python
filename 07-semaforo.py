import os
os.system("cls")

cor = input("fale a cor do semafaro:")

if cor == ("verde"):
    print("pode passar")
elif cor == ("amarelo"):
    print("Atenção")
elif cor == ("vermelho"):
    print("pare")
else:
    print("cor invalida")