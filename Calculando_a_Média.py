#ID 14: Crie uma função que receba uma lista de números e retorne a média aritmética desses valores.

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def media_aritmetica(lista):
    if len(lista) == 0:
        return 0  
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media
print(media_aritmetica(numeros))