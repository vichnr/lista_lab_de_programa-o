#ID 3: Crie uma função que retorne o segundo maior número de uma lista. Considere que a lista pode ter números duplicados.

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def segundo_maior_numero(lista):
    return sorted(set(lista))[-2]
print(segundo_maior_numero(numeros))
