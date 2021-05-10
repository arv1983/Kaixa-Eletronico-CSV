import json
import time
import os
from datetime import date
from json import dump

# arquivo = 'Python E3 - Kaixa eletrônico/transactions.json'

def calculate_balance(filename):
    try:
        with open(filename, 'r') as json_file:
            if os.stat(filename).st_size < 4:
                return []
            dados = json.load(json_file)
            receitas = sum([value['value'] for value in dados if value['transaction_type'] == 'income'])
            despesas = sum([value['value'] for value in dados if value['transaction_type'] == 'outcome'])
            return 'Seu saldo é de: R$ ' + str(receitas - despesas)
    except:
        return []    

def post_transaction(filename, title, transaction_type, value):
    dataTransactions = all_transactions(filename)
    
    try:
        with open(filename, 'w') as json_file:
            post = {"title": title,
            "transaction_type": transaction_type,
            "value": value,
            "date": date.today().strftime("%d/%m/%Y")
            }
            dataTransactions.append(post)
            json.dump(dataTransactions, json_file, indent=4)
            print(post)
            return post

    except:
        return []  

def all_transactions(filename):
    try:
        with open(filename, 'r+') as json_file:
            stats = os.stat(filename)
            if stats.st_size > 4:
                return json.load(json_file)
            else:
                return []
    except:
        return []




# saldo = calculate_balance('Python E3 - Kaixa eletrônico/transactions.json')
# print(saldo)

# transactions = all_transactions('Python E3 - Kaixa eletrônico/transactions.json')
# print(transactions)

# post_transaction('Python E3 - Kaixa eletrônico/transactions.json', 'gastei com222', 'outcome', 1000)
# saldo = calculate_balance('Python E3 - Kaixa eletrônico/transactions.json')
# print(saldo)


# 1 - Você não precisa utilizar sua var global arquivo pois o arquivo já é passado por parâmetro como filename. Apague seus tests internos antes de subir.

# 2 - Sua funções não estão funcionando corretamente em caso de arquivo vazio ou inexistente.