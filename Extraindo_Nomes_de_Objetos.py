#ID 7: Crie uma função que receba uma lista de objetos (onde cada objeto tem um atributo 'nome') e retorne uma nova lista contendo apenas os nomes de cada objeto.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

def pegar_nomes(lista_objetos):
    nomes = []
    for obj in lista_objetos:
        nomes.append(obj.nome)
    return nomes

todos_objetos = []

while True:
    entrada = input("digite um nome (ou digite 'sair' para encerrar): ").strip()
    if entrada.lower() == 'sair':
        break
    objeto = Pessoa(entrada)
    todos_objetos.append(objeto)

lista_nomes = pegar_nomes(todos_objetos)
print(lista_nomes)