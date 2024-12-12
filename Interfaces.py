from Caixa import *

def interface_main():
    '''
    Resumo: Interface principal do programa, onde começa o atendimento de um cliente ou encerra o programa.

    Não tem parâmetro e nem retorna algo
    '''
    while True:
        print(f"[1]Iniciar atendimento\n[2]Finalizar atendimento")
        opcao = input("Opção: ")

        match opcao:
            case "1":
                caixa()
            case "2":
                ganhos_totais()
                verificar_estoque_vazio()
                print("Fechando caixa...")
                break
            case _:
                print("Opção invalida.")