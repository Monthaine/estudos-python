# o codigo abaixo pede para o usuario digitar n numeros e armazena esses numeros em uma lista
# será utilizada def para criar uma função que realiza essa tarefa, que retorna a lista de numeros digitados
def mensagem():
    n = input("Quantos numeros você quer digitar?")
    n = int(n)
    lista = []
# laço para pedir os numeros n vezes 
    for i in range(n):
        numero = input("Digite um numero:")
        numero = int(numero)
        lista.append(numero)
# retorna a lista de numeros digitados
    return lista
# chama a função e armazena o resultado na variavel numeros
numeros = mensagem()
# exibe a lista de numeros digitados
print("Os numeros digitados foram:", numeros)