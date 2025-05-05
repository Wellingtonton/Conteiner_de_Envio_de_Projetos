
import math
from colorama import Fore, Style, init
import locale
import tkinter as tk
from tkinter import messagebox

init(autoreset=True)

# Define o locale para português do Brasil
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')

def formatar_numero(num):
    return locale.format_string('%.2f', num, grouping=True).replace('.', '#').replace(',', '.').replace('#', ',')

def parse_numero(valor):
    return float(valor.replace('.', '').replace(',', '.'))

def calcular_unario(operacao, num):
    match operacao:
        case '√':
            return math.sqrt(num)
        case 'sen':
            return math.sin(math.radians(num))
        case 'cos':
            return math.cos(math.radians(num))
        case 'tan':
            return math.tan(math.radians(num))

def calcular_binario(operacao, num1, num2):
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '^':
            return num1 ** num2

def calcular_porcentagem(tipo, p, valor):
    if tipo == "% de":
        return valor * (p / 100)
    elif tipo == "+%":
        return valor + (valor * (p / 100))
    elif tipo == "-%":
        return valor - (valor * (p / 100))

def exibir_resultado(resultado):
    resultado_var.set(f"Resultado: {formatar_numero(resultado)}")

def realizar_calculo():
    op = operacao_var.get().strip().lower()
    try:
        if op == '%':
            tipo = tipo_porcentagem_var.get().strip()
            p = parse_numero(porcentagem_var.get().strip())
            valor = parse_numero(valor_base_var.get().strip())
            resultado = calcular_porcentagem(tipo, p, valor)
            exibir_resultado(resultado)
        elif op in operacoes_unarias:
            num = parse_numero(entrada_var.get().strip())
            resultado = calcular_unario(op, num)
            exibir_resultado(resultado)
        elif op in operacoes_binarias:
            num1 = parse_numero(entrada_var.get().strip())
            num2 = parse_numero(entrada_var2.get().strip())
            resultado = calcular_binario(op, num1, num2)
            exibir_resultado(resultado)
        else:
            messagebox.showerror("Erro", "Operação inválida!")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Erro: Divisão por zero!")
    except ValueError:
        messagebox.showerror("Erro", "Erro: Entrada inválida, digite apenas números.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado: {e}")

def fechar_janela():
    janela.quit()

def atualizar_campos(*args):
    op = operacao_var.get().strip().lower()
    for widget in [label_entrada2, campo_entrada2,
                   label_porcentagem, campo_porcentagem,
                   label_valor_base, campo_valor_base,
                   label_tipo_pct, campo_tipo_pct]:
        widget.grid_remove()

    if op in operacoes_binarias:
        label_entrada2.grid()
        campo_entrada2.grid()
    elif op == '%':
        label_porcentagem.grid()
        campo_porcentagem.grid()
        label_valor_base.grid()
        campo_valor_base.grid()
        label_tipo_pct.grid()
        campo_tipo_pct.grid()

# Interface gráfica
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.configure(bg="#2E2E2E")

# Variáveis
operacao_var = tk.StringVar()
operacao_var.trace_add("write", atualizar_campos)

tipo_porcentagem_var = tk.StringVar()
porcentagem_var = tk.StringVar()
valor_base_var = tk.StringVar()
entrada_var = tk.StringVar()
entrada_var2 = tk.StringVar()
resultado_var = tk.StringVar()

operacoes_unarias = {'√', 'sen', 'cos', 'tan'}
operacoes_binarias = {'+', '-', '*', '/', '^'}

# Layout fixo
tk.Label(janela, text="Escolha a operação:", bg="#2E2E2E", fg="white").grid(row=0, column=0)
tk.Entry(janela, textvariable=operacao_var).grid(row=0, column=1)

tk.Label(janela, text="Digite o número (ou base):", bg="#2E2E2E", fg="white").grid(row=1, column=0)
tk.Entry(janela, textvariable=entrada_var).grid(row=1, column=1)

# Campos que podem ser ocultos
label_entrada2 = tk.Label(janela, text="Digite o segundo número:", bg="#2E2E2E", fg="white")
campo_entrada2 = tk.Entry(janela, textvariable=entrada_var2)
label_entrada2.grid(row=2, column=0)
campo_entrada2.grid(row=2, column=1)

label_porcentagem = tk.Label(janela, text="Digite a porcentagem:", bg="#2E2E2E", fg="white")
campo_porcentagem = tk.Entry(janela, textvariable=porcentagem_var)
label_porcentagem.grid(row=3, column=0)
campo_porcentagem.grid(row=3, column=1)

label_valor_base = tk.Label(janela, text="Digite a base do valor:", bg="#2E2E2E", fg="white")
campo_valor_base = tk.Entry(janela, textvariable=valor_base_var)
label_valor_base.grid(row=4, column=0)
campo_valor_base.grid(row=4, column=1)

label_tipo_pct = tk.Label(janela, text="Tipo de porcentagem (% de / +% / -%):", bg="#2E2E2E", fg="white")
campo_tipo_pct = tk.Entry(janela, textvariable=tipo_porcentagem_var)
label_tipo_pct.grid(row=5, column=0)
campo_tipo_pct.grid(row=5, column=1)

# Botões
tk.Button(janela, text="Calcular", command=realizar_calculo, bg="green", fg="white").grid(row=6, column=0, columnspan=2)
tk.Label(janela, textvariable=resultado_var, bg="#2E2E2E", fg="white").grid(row=7, column=0, columnspan=2)
tk.Button(janela, text="Sair", command=fechar_janela, bg="red", fg="white").grid(row=8, column=0, columnspan=2)

# Inicia ocultando campos desnecessários
atualizar_campos()

janela.mainloop()
