import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("A CONEXÃO COM O BANCO FOI OCULTA")

db = client.nomedobanco


nomedocumento = {
    "date": datetime.datetime.utcnow(),
    "nome": "Alexandre Nascimento",
    "cpf": "14334567844",
    "endereço": "Rua da Casinha Vazia, 333",
    "conta": "02573-2",
    "agencia": "0001",
    "tipo": "Corrente"
}

nomedacolecao = db.nomedacolecao
lua_id = nomedacolecao.insert_one(nomedocumento).inserted_id

pprint.pprint(db.nomedacolecao.find_one())

#for post in nomedacolecao.find():
#    pprint.pprint(post)
