from pymongo import MongoClient

def conectar_mongo():
    cliente = MongoClient(
        "mongodb+srv://isarangel:01isarafa@lista3bim.5ptiy8e.mongodb.net/?retryWrites=true&w=majority"
    )
    db = cliente["halloween_db"]          # banco de dados do Cofre de Doces
    colecao = db["cofre_doces"]           # coleção para guardar os doces
    return colecao
