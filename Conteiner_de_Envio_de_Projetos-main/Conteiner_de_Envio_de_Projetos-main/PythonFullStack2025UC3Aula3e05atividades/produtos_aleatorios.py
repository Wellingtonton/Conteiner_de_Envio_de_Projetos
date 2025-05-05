import random
from typing import List, Dict

class Produto:
    def __init__(self, nome: str, categoria: str):
        self.nome = nome
        self.categoria = categoria

    def __repr__(self):
        return f"Produto(nome='{self.nome}', categoria='{self.categoria}')"

def gerar_produtos_aleatorios(num_produtos=20) -> List[Produto]:
    """Gera uma lista de produtos aleatórios com categorias variadas."""
    categorias = ["Eletrônicos", "Informática", "Casa", "Alimentos", "Livros", "Esportes"]
    nomes_base = ["Item_A", "Item_B", "Produto_X", "Objeto_Y"]
    produtos = []
    for i in range(num_produtos):
        nome = f"{random.choice(nomes_base)}_{i+1}"
        categoria = random.choice(categorias)
        produtos.append(Produto(nome, categoria))
    return produtos

def contar_produtos_por_categoria(lista_de_produtos: List[Produto]) -> Dict[str, int]:
    """
    Conta a quantidade de produtos em cada categoria usando um dicionário.

    Args:
        lista_de_produtos: Uma lista de objetos Produto.

    Returns:
        Um dicionário onde as chaves são os nomes das categorias e os valores são as quantidades de produtos em cada categoria.
    """
    contagem = {}
    for produto in lista_de_produtos:
        categoria = produto.categoria
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    return contagem

def identificar_duplicatas(lista_de_produtos: List[Produto]) -> List[Produto]:
    """
    Identifica e retorna uma lista de produtos duplicados em uma lista de objetos Produto.
    Considera um produto duplicado se o nome e a categoria forem iguais.
    """
    vistos = set()
    duplicatas = []
    for produto in lista_de_produtos:
        chave = (produto.nome, produto.categoria)
        if chave in vistos:
            duplicatas.append(produto)
        else:
            vistos.add(chave)
    return duplicatas

def main():
    """Função principal para demonstrar a contagem de produtos por categoria e identificação de duplicatas."""
    produtos = gerar_produtos_aleatorios(30) # Aumentando para ter mais chances de duplicatas
    print("Lista de Produtos Gerados:")
    for produto in produtos:
        print(produto)

    contagem_por_categoria = contar_produtos_por_categoria(produtos)
    print("\nContagem de Produtos por Categoria:")
    for categoria, quantidade in contagem_por_categoria.items():
        print(f"Categoria: {categoria}: {quantidade} produtos")

    duplicatas = identificar_duplicatas(produtos)
    if duplicatas:
        print("\nProdutos Duplicados Encontrados (nome e categoria iguais):")
        for produto_duplicado in duplicatas:
            print(produto_duplicado)
    else:
        print("\nNenhum produto duplicado encontrado (nome e categoria iguais).")

if __name__ == "__main__":
    main()