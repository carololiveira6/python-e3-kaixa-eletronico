import json
import os.path
from datetime import datetime
import csv

def all_transactions(filename):

    empty_list = []

    if not filename or not os.path.exists(filename) or not os.stat(filename).st_size:
        return empty_list

    current_file = open(filename)
    data = json.load(current_file)
    current_file.close()

    return data

def post_transaction(filename, title, transaction_type, value):
    
    current_data = all_transactions(filename)
    data_atual = datetime.now()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")
    new_transaction = {"title": title, "transaction_type": transaction_type, "value": value, "date": data_atual_formatada}
    current_data.append(new_transaction)
    
    with open(filename, "w") as file:
        json.dump(current_data, file)
    
    return new_transaction

def calculate_balance(filename):
    
    current_data = all_transactions(filename)
    saldo = 0

    if current_data == []:
        return []

    for data_item in current_data:
        title_data, type_data, value_data, date_data = data_item.values()

        if type_data == 'outcome':
            saldo = saldo - value_data

        if type_data == 'income':
            saldo = saldo + value_data
        
    return f'Seu saldo é de: R$ {saldo}'

if __name__ == "__main__":
    FILENAME = 'transactions.json'

    transactions = all_transactions(FILENAME)
    print(transactions)

    transaction_post = post_transaction(FILENAME, "Salario", 'income', 250)
    print(transaction_post)

    saldo = calculate_balance(FILENAME)
    print(saldo)




# Prototipo de uma tentativa diferente:

# import json
# import os.path

# def all_transactions(filename):
#     empty_list = []
#     if not filename or not os.path.exists(filename) == True:
#         return empty_list
#     else:
#         current_file = open(filename)
#         data = json.load(current_file)
#         current_file.close()
#     return data
# def post_transaction(filename, title, transaction_type, value):
#     current_file = all_transactions(filename)
#     current_file.append({'title': title, 
#         'transaction_type': transaction_type , 
#         'value': value, 
#         'date': '29/01/2021'})
#     with open(filename, 'w') as f:
#         json.dump(current_file, f)
#     return current_file
# post_transaction("./ca.json", "Arroz", "outcome", 200)