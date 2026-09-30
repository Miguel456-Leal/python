import os
os.system("cls")
import time

taxa = 10
taxa2 = 5

veiculos = [
    "Carro R$8,00",
    "Moto R$5,00",
    "SUV R$12,00"
]
while True:
    print("=== Menu Do Estacionamento ===")


    print("[1] Realizar Cobrança")
    print("[2] informações do Estacionamento")
    print("[3] Sair do sistema")

    op_usuario = int(input("selecione um Número:"))

    if (op_usuario == 1):
        print("Você selecionou Realizar cobrança")
    elif(op_usuario == 2):
        print("Informações do estacionamento")
    elif(op_usuario == 3):
        print("saindo do sistema")
    time.sleep(3)

    os.system("cls")
    if(op_usuario == 1):
        print("== Menu de Cobrança ==")
        cliente = input("Informe Seu Nome:")
        tipo_de_veiculo = int(input("""[1] Carro 
[2] moto 
[3]SUV
Qual o tipo do seu veiculo :"""))
        horas =float(input("Coloque a quantidade de horas:"))

        os.system("cls")
        print(f"Cliente: {cliente}")
        print(f"Horas Estacionado: {horas}")

        if(tipo_de_veiculo == 1):
            print("Seu Veiculo:Carro R$8,00")
            valor_basecarro = 8 * horas
            print(f"Valor inicial:{valor_basecarro}")
            print(f"Média por hora {valor_basecarro / horas}")
            if horas >=10:
                        print("taxa adicionada de 10%")
                        valor_fina = valor_basecarro + (valor_basecarro * taxa /100 )
                        print(f"Valor Final:{valor_fina}")
                        break
            elif horas >= 5:
                        print("taxa adicionada de 5%")
                        valor_fina2 = valor_basecarro + (valor_basecarro * taxa2 /100 )
                        print(f"Valor Final:{valor_fina2}")
                        break
            else :
                          print("sem taxa")
            break
            
        
        elif(tipo_de_veiculo == 2):
            print("Seu Veiculo:Moto R$5,00")
            valor_basemoto = 5 * horas
            print(f"Valor inicial:{valor_basemoto}")
            print(f"Média por hora {valor_basemoto / horas}")
            if horas >=10:
                        print("taxa adicionada de 10%")
                        taxa = 10
                        valor_fina = valor_basemoto + (valor_basemoto * taxa /100 )
                        print(f"Valor Final:{valor_fina}")
                        break
            elif horas >= 5:
                        taxa2 = 5
                        print("taxa adicionada de 5%")
                        valor_fina2 = valor_basemoto + (valor_basemoto * taxa2 /100 )
                        print(f"Valor Final:{valor_fina2}")
                        break
            else :
                          print("sem taxa")
            break
        elif(tipo_de_veiculo == 3):
            print("Seu Veiculo:SUV R$12,00")
            valor_baseSUV = 12 * horas
            print(f"Valor inicial:{valor_baseSUV}")
            print(f"Média por hora {valor_baseSUV / horas}")
            if horas >=10:
                                    print("taxa adicionada de 10%")
                                    taxa = 10
                                    valor_fina = valor_baseSUV + (valor_baseSUV * taxa /100 )
                                    print(f"Valor Final:{valor_fina}")
                                    break
            elif horas >= 5:
                                    taxa2 = 5
                                    print("taxa adicionada de 5%")
                                    valor_fina2 = valor_baseSUV + (valor_baseSUV * taxa2 /100 )
                                    print(f"Valor Final:{valor_fina2}")
                                    break
            else :
                                      print("sem taxa")
                                      break
        else:   print("Número invalido ou você digitou algo errado")
        

    elif(op_usuario == 2):
        print("=== Informações do Estacionamento ===")
        for tipos in veiculos:
            print(tipos)
        print("== Sobre Os Horarios ==")
        print("caso o horario de Estacionamento passe ou fique em 5 Horas será adicionado 5% de taxa, acima de 10 Horas 10%.")
        input("\n Precione <ENTER> para Volta ao menu")
        os.system("cls")
    elif(op_usuario == 3):
        print("TEM CERTEZA?")
        resposta = input("informe sua resposta:")
        if resposta == "sim" or "Sim":
            print("Beleza, Saindo")
            break



    

    
