from Caixa import *

def interface_main():
    while True:
        print(f"[1]Iniciar atendimento\n[2]Finalizar atendimento")
        opcao = input("Opção: ")

        match opcao:
            case "1":
                #tarara
                print("Oi")
            case "2":
                #tarata
                print("Imprimindo notas...")
                print("Fechando caixa...")
                break
            case _:
                print("Opção invalida.")