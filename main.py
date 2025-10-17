from database.db import conectar_mongo
collection = conectar_mongo()
from crypto import criptografar, descriptografar
from datetime import datetime

def adicionar_doces():
    child = input("Nome da criança: ")
    candy_type = input("Tipo de doce: ")
    qty = int(input("Quantidade: "))
    
    doc = {
        "child": child,
        "candy_type": criptografar(candy_type),
        "qty": qty,
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(doc)
    print("Doce adicionado com sucesso!\n")

def listar_doces():
    for doc in collection.find():
        print(f"Criança: {doc['child']}")
        print(f"Doce: {descriptografar(doc['candy_type'])}")
        print(f"Quantidade: {doc['qty']}")
        print(f"Data: {doc['timestamp']}\n")

def menu():
    while True:
        print("=== Cofre de Doces ===")
        print("1 - Adicionar doce")
        print("2 - Listar doces")
        print("3 - Sair")
        escolha = input("Escolha: ")
        
        if escolha == "1":
            adicionar_doces()
        elif escolha == "2":
            listar_doces()
        elif escolha == "3":
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
