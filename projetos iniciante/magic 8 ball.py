# o código a seguir simula uma bola mágica 8 que responde a perguntas do usuário.
# primeiramente iremos importar o módulo random para selecionar respostas aleatórias.
import random
# o próximo passo é definir uma lista de respostas possíveis que a 8 ball dará para o usuário.
respostas = [
    "Com certeza!",
    "Não tenho certeza, tente novamente.",
    "Definitivamente não.",
    "Sim, sem dúvida.",
    "Pergunte novamente mais tarde.",
    "Minhas fontes dizem que sim.",
    "Não conte com isso.",
    "É certo.",
    "Concentre-se e pergunte novamente.",
    "Muito duvidoso."
]
# agora, iremos acrescentar uma saudação e vamos criar um loop while true que permita ao usuário fazer perguntas até que ele decida sair.
print("Bem-vindo à Bola Mágica 8!")
while True:
    pergunta = input("Faça uma pergunta (ou digite 'sair' para encerrar): ")
# vamos criar também um método para o usuário sair do loop.
    if pergunta.lower() == 'sair':
        print("Obrigado por jogar! Até a próxima.")
        break
    resposta = random.choice(respostas)
    print("A Bola Mágica 8 diz:", resposta)