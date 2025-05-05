class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produtos_objetos = [
    Produto("Notebook Dell", 1200),
    Produto("Mouse Logitech", 80),
    Produto("Monitor LG", 950),
    Produto("Teclado Mecânico", 250),
    Produto("Smartphone Samsung", 1500),
    Produto("SSD 1TB", 800),
    Produto("Cadeira Gamer", 1100),
]

produtos_objetos_caros = [produto for produto in produtos_objetos if produto.preco > 1000]

print("\nProdutos (objetos) com preço superior a R$ 1000:")
for produto in produtos_objetos_caros:
    print(f"- {produto.nome}: R$ {produto.preco}")