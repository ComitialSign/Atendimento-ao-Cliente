from CsvManager import *
from tabulate import tabulate
from datetime import datetime

lista_de_clientes = [] #Lista os clientes atendidos e quanto gastaram
contador_cliente = 0 # itera o número do cliente

def caixa():
    '''
    Resumo: Loop de uma interface para atender o cliente e imprimir sua nota fiscal

    Não recebe nenhum parâmetro e nem retorna algo
    '''

    lista = [] #lista onde coloca o produto e a quantidade para a nota fiscal

    while True:
        print(f'[1]Passar produto\n[2]Finalizar atendimento do cliente')
        opcao = input("Opção: ")

        match opcao:
            case "1":
                produto_id = input("Digite o ID do produto: ")
                produto = validar_produto(produto_id)
                if produto is None:
                    continue
                quantidade = int(input("Digite a quantidade: "))
                if verificar_quantidade(produto, quantidade):
                    lista.append((produto, quantidade))
            case "2":
                nota_fiscal(lista)
                break
            case _:
                print("Opção invalida")    

def validar_produto(id):
    '''
    Resumo: Verifica o ID do produto para ver se ele existe no CSVe o retorna, caso contrário retorna nada

    Param: ID

    Retorna: O produto ou None
    '''

    dados = ler_dados()

    for item in dados:
        if item['id'] == str(id):
            return item
            
    print(f'Erro: produto não cadastrado.')
    return None

def verificar_quantidade(produto, quantidade):
    '''
    Resumo: Recebe o produto e a sua quantidade, verifica se ele tem a quantidade pedida no estoque e retorna true, caso
    contrário retorna false

    Param: produto e quantidade

    Retorna: True ou False
    '''

    dados = ler_dados()

    for item in dados:
        item == produto
        if quantidade == 0:
            print('Erro: quantidade deve ser maior que zero')
            return False
        elif int(produto['quantidade']) < quantidade:
            print('Erro: quantidade indisponivel em estoque')
            return False
        else:
            produto['quantidade'] = str(int(produto['quantidade']) - quantidade)
            atualizar_estoque(produto)
            return True

def atualizar_estoque(produto_atualizado):
    '''
    Resumo: Atualiza o estoque no arquivo CSV quando um produto é retirado

    Param: O produto

    Não tem retorno
    '''

    dados = ler_dados()

    for item in dados:
        if item['id'] == produto_atualizado['id']:
            item['quantidade'] = produto_atualizado['quantidade']
            break

    salvar_dados(dados)

def nota_fiscal(produtos):
    '''
    Resumo: Printa a nota fiscal do produto do que o Cliente comprou. A nota contém qual o cliente, a data e a hora, 
    os produtos comprados e o total gasto.  

    Param: lista com os produtos

    Não tem retorno
    '''

    if not produtos:
        return

    global contador_cliente 
    
    contador_cliente += 1

    table = []
    gasto_total = 0
    for index, (produto, quantidade) in enumerate(produtos, start=1):
        total = int(produto['preco']) * quantidade
        table.append([index, produto['nome'], quantidade, produto['preco'], total])
        gasto_total += total        

    lista_de_clientes.append((contador_cliente, gasto_total))
    print("Imprimindo nota fiscal...")
    print(f'Cliente {contador_cliente}\n{get_date()}')
    print()
    print(tabulate(table, headers=['Item', 'Produto', 'Quant.', 'Preço', 'Total']))
    print()
    print(f'Itens: {int(len(produtos))}\nTotal: {gasto_total}')

def ganhos_totais():
    '''
    Resumo: Ao fechar o caixa, vai printar cada cliente e o quanto cada gastou no total, além do faturamento total
    do caixa.

    Não recebe parâmetro e nem retorna algo.
    '''

    if not lista_de_clientes:
        return

    table = []
    ganho_total = 0
    for cliente_id, total in lista_de_clientes:
        table.append([f'Cliente {cliente_id}', total])
        ganho_total += total

    print("Imprimindo os ganhos...")
    print(f'Fechamento do caixa\n{get_date()}')
    print()
    print(tabulate(table, headers=['Cliente', 'Total']))
    print()
    print(f'Total de vendas: {ganho_total}')

def get_date():
    '''
    Resumo: Pega a data e a hora, formata e a retorna

    Não tem parâmetro

    Retorna: a Data e a hora formatada no padrão dd/mm/YY H:M
    '''

    date = datetime.now()
    formated_date = date.strftime("%d/%m/%Y %H:%M")

    return formated_date

def verificar_estoque_vazio():
    '''
    Resumo: Verifica quais produtos do estoque estão vazios e os printa ao fechar o caixa

    Não tem parâmetro e nem retorna algo
    '''

    dados = ler_dados()

    produtos_sem_estoque = []

    for item in dados:
        if int(item['quantidade']) == 0:
            produtos_sem_estoque.append(item['nome'])

    if produtos_sem_estoque:
        print('Produtos sem estoque: ')
        for i in produtos_sem_estoque:
            print(i)