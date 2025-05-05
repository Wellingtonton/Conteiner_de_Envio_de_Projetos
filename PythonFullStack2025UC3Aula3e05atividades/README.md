# Projeto de Gerenciamento Integrado (Estoque e Colaboradores)

 Este repositório contém um projeto em Python que demonstra um sistema de gerenciamento de estoque,  produtos, (filtro (dados_produtos_json.py)) e um sistema de gerenciamento de colaboradores. Os arquivos meu_projeto.py, produtos_aleatorios.py, dados_produtos_json.py e gerenciador_colaboradores.py trabalham em conjunto, interagindo para oferecer funcionalidades integradas através de um menu principal.

## Arquivos Principais:

* `meu_projeto.py`: O arquivo principal que serve como ponto de entrada do sistema. Ele apresenta um menu interativo para acessar as funcionalidades de estoque e colaboradores.
* `produtos_aleatorios.py`: Contém a lógica para gerar produtos aleatórios, utilizados para inicializar o sistema caso não haja dados salvos. Também pode conter a definição da classe `Produto`.
* `gerenciador_colaboradores.py`: Implementa as funcionalidades de gerenciamento de colaboradores (adicionar, buscar por ID, listar por salário). Os dados dos colaboradores são mantidos em memória durante a execução.
* `dados_produtos.json`: (Criado durante a execução) Armazena os dados persistentes dos produtos.

## Interação:

Ao executar `meu_projeto.py`, o usuário pode navegar por diferentes menus para gerenciar o estoque de produtos (listar, adicionar, atualizar, procurar, filtrar, contar por categoria) e os colaboradores (adicionar, buscar, listar por salário). Os diferentes arquivos de código trabalham em conjunto para fornecer essa experiência integrada.

Este projeto demonstra a capacidade de modularizar diferentes aspectos de um sistema e integrá-los através de uma interface de usuário centralizada.