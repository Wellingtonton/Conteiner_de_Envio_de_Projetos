from collections import defaultdict

def contar_estoque_por_categoria(estoque):
    """
    Conta a quantidade de produtos em estoque por categoria.

    Args:
        estoque (list): Uma lista de dicionários, onde cada dicionário
                       representa um produto e contém a chave 'categoria'.

    Returns:
        dict: Um dicionário onde as chaves são as categorias e os valores
              são o número de produtos em cada categoria.
    """
    contagem = defaultdict(int)
    for produto in estoque:
        categoria = produto.get('categoria')
        if categoria:
            contagem[categoria] += 1
        else:
            print(f"Aviso: Produto sem categoria definida: {produto.get('nome', 'Sem nome')}")
    return dict(contagem)

# Exemplo de estoque (o mesmo de antes)
estoque_produtos = [
    {'nome': 'Camiseta Azul', 'categoria': 'Vestuário'},
    {'nome': 'Calça Jeans', 'categoria': 'Vestuário'},
    {'nome': 'Tênis Corrida', 'categoria': 'Calçados'},
    {'nome': 'Sandália Praia', 'categoria': 'Calçados'},
    {'nome': 'Livro Python', 'categoria': 'Livros'},
    {'nome': 'Livro Java', 'categoria': 'Livros'},
    {'nome': 'Boné Aba Reta', 'categoria': 'Acessórios'},
    {'nome': 'Mochila Esportiva', 'categoria': 'Acessórios'},
    {'nome': 'Meias Cano Alto', 'categoria': 'Vestuário'},
    {'nome': 'Produto sem categoria', 'preco': 25.00}, # Produto sem categoria
]

resultado_contagem = contar_estoque_por_categoria(estoque_produtos)
print(resultado_contagem)