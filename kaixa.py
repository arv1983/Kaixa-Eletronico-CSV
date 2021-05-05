import json
import time
import os
from datetime import date
from json import dump

arquivo = "Python E3 - Kaixa eletrônico/transactions.json"

def calculate_balance(filename):
    with open(filename, 'r') as json_file:
        dados = json.load(json_file)
        receitas = sum([value['value'] for value in dados if value['transaction_type'] == 'income'])
        despesas = sum([value['value'] for value in dados if value['transaction_type'] == 'outcome'])
        return 'Seu saldo é de R$ ' + str(receitas - despesas)
        

def post_transaction(filename, title, transaction_type, value):
    tudo = all_transactions(filename)
    with open(filename, 'w') as json_file:
        post = {"title": title,
        "transaction_type": transaction_type,
        "value": value,
        "date": date.today().strftime("%d/%m/%Y")
        }
        tudo.append(post)
        json.dump(tudo, json_file, indent=4)
        return post

def all_transactions(filename):
    stats = os.stat(arquivo)
    if os.stat(filename) and stats.st_size > 4:
        return json.load(open(filename, 'r'))
    else:
        return []

# transactions = all_transactions(arquivo)
# print(transactions)



# post_transaction(arquivo, 'gastei com222', 'outcome', 1000)
# saldo = calculate_balance(arquivo)
# print(saldo)
