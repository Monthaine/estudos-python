#o código a seguir demonstra o uso de listas em Python.
#uma lista é uma coleção ordenada e mutável de itens.
#primeiro passo será criar uma lista vazia e adicionar alguns números a ela. Será solicitado ao usuário que insira a quantidade de números que deseja adicionar à lista.
lista = []
n = int(input("Quantos números você quer adicionar à lista? "))
# a seguir, usaremos um loop for para adicionar os números à lista.
for i in range(n):
    lista.append(int(input("Digite um número: "))) 
#agora, vamos exibir a lista completa.
print("A lista completa é:", lista)
#em seguida, vamos calcular a soma, média, maior valor, menor valor e o tamanho da lista.
soma = sum(lista)
tamanho= len(lista)
media = soma / tamanho if tamanho > 0 else 0
maior = max(lista) if tamanho > 0 else None
menor = min(lista) if tamanho > 0 else None
#finalmente, exibimos os resultados.
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Tamanho da lista: {tamanho}")
#o código também verifica se cada número na lista é par ou ímpar.
for numero in lista:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")