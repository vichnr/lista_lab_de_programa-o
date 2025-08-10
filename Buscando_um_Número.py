#ID 6: Elabore uma função que receba um número e uma lista. A função deve buscar o número na lista e retornar 'True' se o encontrar e 'False' caso contrário.

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def buscar_numero(numero, lista):
    return numero in lista
usuario = int(input("Digite um número para buscar: "))
print(buscar_numero(usuario, numeros))