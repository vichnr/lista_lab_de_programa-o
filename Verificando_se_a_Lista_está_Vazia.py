#ID 11: Escreva uma função que receba uma lista e retorne 'True' se ela estiver vazia e 'False' caso contrário.

lista = []

x = input("digite algo (ou pressione enter para sair): ").lower().strip()
if x != "":
    lista.append(x)

def vazia(lista):
    vazio = False
    if len(lista) == 0:
        vazio = True
    return vazio

print(vazia(lista))