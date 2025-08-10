#ID 13:Desenvolva uma função que receba uma lista de números e retorne o menor número encontrado nela.

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def menor_numero(lista):
    if len(lista) == 0:
        return None  # Caso a lista seja vazia, retorna None
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor
print(menor_numero(numeros))
