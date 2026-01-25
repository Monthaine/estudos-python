# Neste projeto vamos criar um chatbot simples usando a API da OpenAI.
# Certifique-se de ter a biblioteca openai instalada:
# python -m pip install openai
import os
from openai import OpenAI
# Após isso, o cliente pode ser criado e usado para interagir com o modelo de linguagem.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# O histórico será usado para manter o contexto da conversa.
historico = [{"role": "system", "content": "Você é um chatbot educado e prestativo."}]
# Utilizaremos um loop infinito para interagir com o usuário.
while True:
    # Solicita a mensagem do usuário.
    mensagem = input("Você: ")
    # Verifica se o usuário quer sair do chat.
    if mensagem.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chatbot. Até mais!")
        break
# Adiciona a mensagem do usuário ao histórico.
    historico.append({"role": "user", "content": mensagem})
# Cria a resposta do modelo usando o histórico da conversa.
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=historico
    )
# Extrai o conteúdo da resposta do bot.
    resposta_bot = resposta.choices[0].message.content
# Adiciona a resposta do bot ao histórico.
    historico.append({"role": "assistant", "content": resposta_bot})   
# Exibe a resposta do bot para o usuário.
    print("Bot:", resposta_bot)
