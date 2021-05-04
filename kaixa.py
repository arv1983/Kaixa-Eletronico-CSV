import json
import time
import os
from datetime import date
from json import dump

hoje = date.today().strftime("%d/%m/%Y")
arquivo = "Python E3 - Kaixa eletrônico/transactions.json"

def calculate_balance(filename):
    dados = json.load(open(filename, 'r'))
    receitas = sum([value['value'] for value in dados if value['transaction_type'] == 'income'])
    despesas = sum([value['value'] for value in dados if value['transaction_type'] == 'outcome'])
    return 'Seu saldo é de R$ ' + str(receitas - despesas)

def post_transaction(filename, title, transaction_type, value):
    dados = json.load(open(filename, 'r'))
    post = {"title": title,
        "transaction_type": transaction_type,
        "value": value,
        "date": hoje
    }
    dados.append(post)
    with open(filename, 'w') as json_file:
        json.dump(dados, json_file, indent=4)
  
def all_transactions(filename):
    stats = os.stat(arquivo)
    print(stats.st_size)
    if os.stat(filename) and stats.st_size > 4:
        return json.load(open(filename, 'r'))
    else:
        return []

transactions = all_transactions(arquivo)
print(transactions)

post_transaction(arquivo, 'gastei com222', 'outcome', 1000)
saldo = calculate_balance(arquivo)
print(saldo)
