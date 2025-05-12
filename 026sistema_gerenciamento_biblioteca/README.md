# Sistema de Gerenciamento de Biblioteca

Este programa simples em Python simula o funcionamento básico de um sistema de gerenciamento de biblioteca. Ele permite cadastrar livros e usuários, consultar informações, e realizar o empréstimo de livros.

## Como Funciona

De forma resumida, o sistema organiza as informações da biblioteca através de algumas categorias principais:

* **Livro:** Representa um livro físico com título, autor, ISBN e sua disponibilidade.
* **Usuário:** Representa uma pessoa cadastrada na biblioteca com nome e um ID único.
* **Empréstimo:** Registra quando um livro é emprestado a um usuário, guardando o livro e o usuário envolvidos.
* **Biblioteca:** É quem gerencia tudo! Ela guarda a lista de livros, usuários e os empréstimos realizados. A `Biblioteca` tem funcionalidades para cadastrar, consultar, emprestar e excluir itens.

Ao executar o programa, um menu interativo é apresentado, permitindo que você escolha as seguintes ações:

1.  **Cadastrar Livro:** Adiciona um novo livro à biblioteca, pedindo o título, autor e ISBN.
2.  **Cadastrar Usuário:** Adiciona um novo usuário ao sistema, solicitando o nome e um ID.
3.  **Consultar Livros Cadastrados:** Mostra todos os livros que foram cadastrados.
4.  **Consultar Usuários Cadastrados:** Exibe todos os usuários registrados no sistema.
5.  **Consultar Livro por ISBN:** Permite buscar um livro específico usando o seu ISBN.
6.  **Emprestar Livro:** Permite registrar o empréstimo de um livro para um usuário (o livro precisa estar disponível).
7.  **Excluir Livro:** Remove um livro da biblioteca usando o seu ISBN.
8.  **Excluir Usuário:** Remove um usuário do sistema usando o seu ID.
9.  **Sair:** Encerra o programa.
    
