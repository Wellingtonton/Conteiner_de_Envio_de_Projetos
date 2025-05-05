import random
from typing import List, Dict, Optional
import os
import json
from collections import defaultdict

# Supondo que produtos_aleatorios.py ainda existe e contém as classes e funções necessárias
try:
    from produtos_aleatorios import Produto, gerar_produtos_aleatorios
    def contar_produtos_por_categoria(lista_de_produtos: List[Produto]) -> Dict[str, int]:
        """Conta a quantidade de produtos em uma lista por categoria."""
        contagem = defaultdict(int)
        for produto in lista_de_produtos:
            categoria = produto.categoria
            contagem[categoria] += 1
        return dict(contagem)
except ImportError:
    print("Erro: O arquivo 'produtos_aleatorios.py' não foi encontrado. Certifique-se de que ele está no mesmo diretório.")
    exit()

# Importando as funções do gerenciador de colaboradores (assumindo que o arquivo se chama gerenciador_colaboradores.py)
try:
    from gerenciador_colaboradores import menu_gerenciamento_colaboradores, Colaborador
    cadastro_de_colaboradores: Dict[int, Colaborador] = {} # Inicializa o cadastro de colaboradores
except ImportError:
    print("Erro: O arquivo 'gerenciador_colaboradores.py' não foi encontrado. Certifique-se de que ele está no mesmo diretório.")
    exit()

DATABASE_FILE = "dados_produtos.json" # Alterado para dados_produtos.json

def carregar_produtos():
    """Carrega os produtos do arquivo JSON, se existir."""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            data = json.load(f)
            return [Produto(p['nome'], p['categoria']) for p in data]
    return gerar_produtos_aleatorios()

def salvar_produtos(lista_de_produtos: List[Produto]):
    """Salva a lista de produtos no arquivo JSON."""
    data = [{'nome': p.nome, 'categoria': p.categoria} for p in lista_de_produtos]
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("Dados dos produtos salvos com sucesso!")

def listar_produtos(lista_de_produtos: List[Produto]):
    """Lista todos os produtos."""
    if not lista_de_produtos:
        print("Não há produtos cadastrados.")
        return
    print("\n--- Lista de Produtos ---")
    for i, produto in enumerate(lista_de_produtos):
        print(f"{i+1}. {produto}")
    print("-------------------------\n")

def adicionar_produto(lista_de_produtos: List[Produto]):
    """Adiciona um novo produto."""
    nome = input("Digite o nome do novo produto: ")
    categoria = input("Digite a categoria do novo produto: ")
    novo_produto = Produto(nome, categoria)
    lista_de_produtos.append(novo_produto)
    salvar_produtos(lista_de_produtos)
    print(f"Produto '{nome}' adicionado com sucesso!")

def atualizar_produto(lista_de_produtos: List[Produto]):
    """Atualiza um produto existente."""
    if not lista_de_produtos:
        print("Não há produtos para atualizar.")
        return
    listar_produtos(lista_de_produtos)
    try:
        indice = int(input("Digite o número do produto que deseja atualizar: ")) - 1
        if 0 <= indice < len(lista_de_produtos):
            produto = lista_de_produtos[indice]
            novo_nome = input(f"Novo nome para '{produto.nome}' (deixe em branco para manter): ")
            nova_categoria = input(f"Nova categoria para '{produto.categoria}' (deixe em branco para manter): ")
            if novo_nome:
                produto.nome = novo_nome
            if nova_categoria:
                produto.categoria = nova_categoria
            salvar_produtos(lista_de_produtos)
            print(f"Produto '{produto.nome}' atualizado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def procurar_produto(lista_de_produtos: List[Produto]):
    """Procura produtos por nome ou categoria."""
    if not lista_de_produtos:
        print("Não há produtos para procurar.")
        return
    termo = input("Digite o nome ou a categoria do produto que você procura: ").lower()
    resultados = [
        produto for produto in lista_de_produtos
        if termo in produto.nome.lower() or termo in produto.categoria.lower()
    ]
    if resultados:
        print("\n--- Resultados da Busca ---")
        for produto in resultados:
            print(produto)
        print("---------------------------\n")
    else:
        print(f"Nenhum produto encontrado com o termo '{termo}'.")

def filtrar_produtos_por_preco(lista_de_produtos: List[Produto]):
    """Filtra produtos com preço superior a 1000."""
    produtos_caros = [produto for produto in lista_de_produtos if hasattr(produto, 'preco') and produto.preco > 1000]
    if produtos_caros:
        print("\n--- Produtos com preço superior a R$ 1000 ---")
        for produto in produtos_caros:
            print(f"- Nome: {produto.nome}, Preço: R$ {produto.preco}")
        print("---------------------------------------------\n")
    else:
        print("Nenhum produto com preço superior a R$ 1000 encontrado.")

def menu_estoque(lista_de_produtos: List[Produto]):
    """Menu para interações relacionadas ao estoque."""
    while True:
        print("\n--- Menu de Estoque ---")
        print("1. Contar produtos por categoria")
        print("0. Voltar ao menu principal")
        print("-------------------------\n")
        opcao_estoque = input("Digite o número da opção desejada: ")

        if opcao_estoque == '1':
            contagem = contar_produtos_por_categoria(lista_de_produtos)
            print("\n--- Contagem de Produtos por Categoria ---")
            for categoria, quantidade in contagem.items():
                print(f"Categoria: {categoria}: {quantidade} produtos")
            print("-----------------------------------------\n")
        elif opcao_estoque == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produtos(lista_de_produtos: List[Produto]):
    """Menu para gerenciar produtos."""
    while True:
        print("\n--- Menu de Produtos ---")
        print("1. Listar produtos")
        print("2. Adicionar produto")
        print("3. Atualizar produto")
        print("4. Procurar produto")
        print("0. Voltar ao menu principal")
        print("------------------------\n")
        opcao_produtos = input("Digite o número da opção desejada: ")

        if opcao_produtos == '1':
            listar_produtos(lista_de_produtos)
        elif opcao_produtos == '2':
            adicionar_produto(lista_de_produtos)
        elif opcao_produtos == '3':
            atualizar_produto(lista_de_produtos)
        elif opcao_produtos == '4':
            procurar_produto(lista_de_produtos)
        elif opcao_produtos == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_filtros(lista_de_produtos: List[Produto]):
    """Menu para opções de filtragem de produtos."""
    while True:
        print("\n--- Menu de Filtros ---")
        print("1. Filtrar produtos com preço > 1000")
        print("0. Voltar ao menu principal")
        print("-------------------------\n")
        opcao_filtros = input("Digite o número da opção desejada: ")

        if opcao_filtros == '1':
            filtrar_produtos_por_preco(lista_de_produtos)
        elif opcao_filtros == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_principal():
    """Exibe o menu principal."""
    print("\n--- Menu Principal ---")
    print("1. Menu de Estoque")
    print("2. Menu de Produtos")
    print("3. Menu de Filtros")
    print("4. Menu de Colaboradores") # Nova opção!
    print("5. Salvar e Sair")
    print("0. Sair sem salvar")
    print("----------------------\n")

def main_terminal():
    """Função principal para a interação via terminal com menus separados."""
    lista_de_produtos = carregar_produtos()

    while True:
        exibir_menu_principal()
        opcao_principal = input("Digite o número da opção desejada: ")

        if opcao_principal == '1':
            menu_estoque(lista_de_produtos)
        elif opcao_principal == '2':
            menu_produtos(lista_de_produtos)
        elif opcao_principal == '3':
            menu_filtros(lista_de_produtos)
        elif opcao_principal == '4':
            menu_gerenciamento_colaboradores(cadastro_de_colaboradores) # Chama o menu de colaboradores
        elif opcao_principal == '5':
            salvar_produtos(lista_de_produtos)
            break
        elif opcao_principal == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_terminal()