from CsvManager import *

def atender_cliente():
    dados = ler_dados()

def passar_produto():
    while True:
        print(f'[1]Passar produto\n[2]Finalizar Atendimento')
        opcao = input("Opção: ")

        match opcao:
            case "1":
                produto_id = input("Digite o ID do produto: ")
                produto = validar_produto(produto_id)
                quantidade = int(input("Digite a do produto: "))
                verificar_quantidade(produto, quantidade)
            case "2":
                break
            case _:
                print("Opção invalida")

def validar_produto(id):
    dados = ler_dados()

    for item in dados:
        if item['id'] == str(id):
            return item
            
    print(f'Erro: produto não cadastrado.')
    return None

def verificar_quantidade(produto, quantidade):
    dados = ler_dados()

    for item in dados:
        item == produto
        if int(produto['quantidade']) == 0:
            print('Erro: quantidade deve ser maior que zero')
        elif int(produto['quantidade']) < quantidade:
            print('Erro: quantidade indisponivel em estoque')
        else:
            produto['quantidade'] = str(int(produto['quantidade']) - quantidade)
            atualizar_estoque(produto)
            break
    
    salvar_dados()

def atualizar_estoque(produto_atualizado):
    dados = ler_dados()

    for item in dados:
        if item['id'] == produto_atualizado['id']:
            item['quantidade'] = produto_atualizado['quantidade']
            break

    salvar_dados

    