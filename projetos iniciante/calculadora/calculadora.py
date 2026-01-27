import tkinter as tk

# iniciamos o projeto configurando a janela principal da calculadora
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("360x420")
janela.resizable(False, False)

modo_escuro = False
botoes_widgets = []

# configurando o container principal
container = tk.Frame(janela, padx=10, pady=10)
container.pack(expand=True, fill="both")

# agora configuramos o visual e o visor da calculadora
topo = tk.Frame(container)
topo.pack(fill="x", pady=(5, 15))

topo.columnconfigure(0, weight=1)

entrada = tk.Entry(
    topo,
    font=('Segoe UI', 26),
    justify="right"
)
entrada.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

# antes de inserir  os botões principais da calculadora, criei a função para alternar o tema entre claro e escuro
def alternar_tema():
    global modo_escuro
    modo_escuro = not modo_escuro

    if modo_escuro:
        bg = "#1e1e1e"
        fg = "white"
        botao_bg = "#2d2d2d"
        botao_tema.config(text="Escuro")
    else:
        bg = "white"
        fg = "black"
        botao_bg = "white"
        botao_tema.config(text="Claro")

    janela.configure(bg=bg)
    container.configure(bg=bg)
    topo.configure(bg=bg)
    grade.configure(bg=bg)
    entrada.configure(bg=botao_bg, fg=fg, insertbackground=fg)

    for botao in botoes_widgets:
        botao.configure(bg=botao_bg, fg=fg)

# criei um botão de tema para poder alternar
botao_tema = tk.Button(
    topo,
    text="Escuro",
    font=('Segoe UI', 10),
    width=7,
    relief="flat",
    command=alternar_tema
)
botao_tema.grid(row=0, column=1)

# o próximo passo é criar a grade de botões
grade = tk.Frame(container)
grade.pack(expand=True, fill="both")

botoes = [
    ('C', 0, 0), ('⌫', 0, 1), ('*', 0, 2), ('/', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('=', 3, 3),
    ('0', 4, 0), ('.', 4, 1)
]

#o próximo passo é criar as funções dos botões e adicionar os botões na grade

for i in range(4):
    grade.grid_columnconfigure(i, weight=1, uniform="x")

for i in range(5):
    grade.grid_rowconfigure(i, weight=1, uniform="y")

def clicar(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def apagar_ultimo():
    entrada.delete(len(entrada.get()) - 1)

def calcular_expressao(expr):
    # remove espaços
    expr = expr.replace(" ", "")

    # separa números e operadores
    numeros = []
    operadores = []
    numero_atual = ""

    for c in expr:
        if c.isdigit() or c == ".":
            numero_atual += c
        else:
            numeros.append(float(numero_atual))
            operadores.append(c)
            numero_atual = ""

    numeros.append(float(numero_atual))

    i = 0
    while i < len(operadores):
        if operadores[i] == "*":
            numeros[i] *= numeros[i + 1]
            numeros.pop(i + 1)
            operadores.pop(i)
        elif operadores[i] == "/":
            numeros[i] /= numeros[i + 1]
            numeros.pop(i + 1)
            operadores.pop(i)
        else:
            i += 1

    resultado = numeros[0]
    for i, op in enumerate(operadores):
        if op == "+":
            resultado += numeros[i + 1]
        elif op == "-":
            resultado -= numeros[i + 1]

    return resultado


def calcular():

    try:
        expressao = entrada.get()
        resultado = calcular_expressao(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def calcular_enter(event):
    calcular()

entrada.bind("<Return>", calcular_enter)

def animar(botao):
    cor = botao.cget("bg")
    botao.configure(bg="#cccccc")
    botao.after(100, lambda: botao.configure(bg=cor))

for texto, linha, coluna in botoes:
    if texto == '=':
        comando = calcular
    elif texto == 'C':
        comando = limpar
    elif texto == '⌫':
        comando = apagar_ultimo
    else:
        comando = lambda x=texto: clicar(x)

    botao = tk.Button(
        grade,
        text=texto,
        font=('Segoe UI', 14),
        relief="flat",
        command=lambda c=comando: c()
    )

    botao.bind("<Button-1>", lambda e, b=botao: animar(b))

    if texto == '=':
        botao.configure(
            bg="#4CAF50",
            fg="white",
            font=('Segoe UI', 16, 'bold')
        )
        botao.grid(
            row=linha,
            column=coluna,
            rowspan=2,
            sticky="nsew",
            padx=4,
            pady=4
        )
    else:
        botao.grid(
            row=linha,
            column=coluna,
            sticky="nsew",
            padx=4,
            pady=4
        )

    botoes_widgets.append(botao)
# essa linha aplica o tema inicial
alternar_tema()

janela.mainloop()
