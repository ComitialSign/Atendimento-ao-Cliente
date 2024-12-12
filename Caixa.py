from CsvManager import *
from tabulate import tabulate
from datetime import datetime

def atender_cliente():
    novo_cliente()
    caixa()



def caixa():
    lista = []

    while True:
        print(f'[1]Passar produto\n[2]Finalizar atendimento do cliente')
        opcao = input("Opção: ")

        match opcao:
            case "1":
                produto_id = input("Digite o ID do produto: ")
                produto = validar_produto(produto_id)
                quantidade = int(input("Digite a do produto: "))
                verificar_quantidade(produto, quantidade)
                lista.append(produto, quantidade)
            case "2":
                nota_fiscal(lista)
                print("Imprimindo nota fiscal...")
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

def nota_fiscal(produtos):
    lista = []
    num_cliente = novo_cliente()
    date = datetime.now()
    formated_date = date.strftime("%d/%m/%Y %H:%M:")

    lista.append(produtos)

    item = 0
    gasto_total = 0
    for sublista in lista:
        for i in sublista:
            item += 1
            produto = i[0]
            total = float(produto['preco']) * i[1]
            table = [[item, produto['nome'], i[1], produto['preco'], total]]
            gasto_total += total


    print(f'Cliente {num_cliente}\n{formated_date}')
    print()
    print(tabulate(table, headers=['Item', 'Produto', 'Quant.', 'Preço', 'Total']))
    print()
    print(f'Itens: {int(len(lista)) + 1}\nTotal: {gasto_total}')

    
def novo_cliente():
    contador = 0

    return contador + 1