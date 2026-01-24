#nesse caso iremos estudar condições utilizando o if, else e elif.
#O if é utilizado para criar uma condição que, se verdadeira, executa um bloco de código.
#O elif é utilizado para criar múltiplas condições, onde se a primeira condição for falsa, a próxima condição será verificada.
#O else é utilizado para criar um bloco de código que será executado se a condição do if for falsa.

num = int(input("Digite um número: "))

if num > 0:
    print(f"O número {num} é positivo.")
elif num < 0:
    print(f"O número {num} é negativo.")
else:
    print("O número é zero.")

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")