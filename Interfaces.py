from Caixa import *

def interface_main():
    while True:
        print(f"[1]Iniciar atendimento\n[2]Finalizar atendimento")
        opcao = input("Opção: ")

        match opcao:
            case "1":
                atender_cliente()
            case "2":
                print("Imprimindo notas...")
                #imprimir_notas
                print("Fechando caixa...")
                break
            case _:
                print("Opção invalida.")