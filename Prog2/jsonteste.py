import json


# d = {'first_name': 'Guido','second_name': 'Rossum','titles': ['BDFL', 'Developer'],}
# with open('meu_arquivo.json', 'w') as f:
#     json.dumps(d)



def escrever_json(lista):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(lista, f,indent=4,)

def carregar_json(arquivo):
    with open('meu_arquivo.json', 'r') as f:
        return json.load(f)

minha_lista = {'first_name': 'Guido','second_name': 'Rossum','titles': ['BDFL', 'Developer'],}
escrever_json(minha_lista)

print(carregar_json('meu_arquivo.json'))