import csv

ARQUIVO_CSV = 'produto.csv'

def ler_dados():
    with open(ARQUIVO_CSV, mode='r', newline='', encoding='utf-8') as file:
        return[row for row in csv.DictReader(file)]
    
def salvar_dados(dados):
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)

