import os 
os.system("cls")

print("== pedagio ==")

pedagio = int(input("qual desse veiculos e o seu 1-carro 2-moto 3-caminhão:"))

if pedagio == 1:
    print ("carro R$10,00")
elif pedagio == 2:
    print("moto R$5,00")
elif pedagio == 3:
    print("caminhão R$20,00")
else:
    print("número invalido ou você digitou uma letra")