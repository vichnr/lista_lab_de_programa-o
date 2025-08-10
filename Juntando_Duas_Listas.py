#ID 12:Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas.

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def juntar_listas(lista1, lista2):
    return lista1 + lista2
cl = juntar_listas(natureza, tecnologia)
print(cl)