class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn} ({status})"

class Usuario:
    def __init__(self, nome, usuario_id):
        self.nome = nome
        self.usuario_id = usuario_id

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.usuario_id}"

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = "09/05/2025" # Simulação da data
        livro.disponivel = False

    def __str__(self):
        return f"Livro: {self.livro.titulo} (ISBN: {self.livro.isbn}), Usuário: {self.usuario.nome} (ID: {self.usuario.usuario_id}), Emprestado em: {self.data_emprestimo}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        livro = Livro(titulo, autor, isbn)
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        usuario_id = input("Digite o ID do usuário: ")
        usuario = Usuario(nome, usuario_id)
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso.")

    def consultar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("\n--- Livros Cadastrados ---")
        for livro in self.livros:
            print(livro)
        print("--------------------------")

    def consultar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("\n--- Usuários Cadastrados ---")
        for usuario in self.usuarios:
            print(usuario)
        print("---------------------------")

    def consultar_livro_por_isbn(self):
        isbn_consulta = input("Digite o ISBN do livro que deseja consultar: ")
        for livro in self.livros:
            if livro.isbn == isbn_consulta:
                print("\n--- Livro Encontrado ---")
                print(livro)
                print("------------------------")
                return
        print(f"Livro com ISBN '{isbn_consulta}' não encontrado.")

    def emprestar_livro(self):
        isbn_emprestimo = input("Digite o ISBN do livro a ser emprestado: ")
        usuario_id_emprestimo = input("Digite o ID do usuário que fará o empréstimo: ")
        livro_para_emprestar = None
        usuario_para_emprestar = None

        for livro in self.livros:
            if livro.isbn == isbn_emprestimo and livro.disponivel:
                livro_para_emprestar = livro
                break
            elif livro.isbn == isbn_emprestimo and not livro.disponivel:
                print(f"O livro com ISBN '{isbn_emprestimo}' não está disponível para empréstimo.")
                return

        for usuario in self.usuarios:
            if usuario.usuario_id == usuario_id_emprestimo:
                usuario_para_emprestar = usuario
                break

        if livro_para_emprestar and usuario_para_emprestar:
            emprestimo = Emprestimo(livro_para_emprestar, usuario_para_emprestar)
            self.emprestimos.append(emprestimo)
            print(f"Livro '{livro_para_emprestar.titulo}' emprestado para '{usuario_para_emprestar.nome}' em {emprestimo.data_emprestimo}.")
        else:
            if not livro_para_emprestar:
                print(f"Livro com ISBN '{isbn_emprestimo}' não encontrado ou não disponível.")
            if not usuario_para_emprestar:
                print(f"Usuário com ID '{usuario_id_emprestimo}' não encontrado.")

    def excluir_livro(self):
        isbn_excluir = input("Digite o ISBN do livro que deseja excluir: ")
        for i, livro in enumerate(self.livros):
            if livro.isbn == isbn_excluir:
                del self.livros[i]
                print(f"Livro com ISBN '{isbn_excluir}' excluído com sucesso.")
                return
        print(f"Livro com ISBN '{isbn_excluir}' não encontrado.")

    def excluir_usuario(self):
        usuario_id_excluir = input("Digite o ID do usuário que deseja excluir: ")
        for i, usuario in enumerate(self.usuarios):
            if usuario.usuario_id == usuario_id_excluir:
                del self.usuarios[i]
                print(f"Usuário com ID '{usuario_id_excluir}' excluído com sucesso.")
                return
        print(f"Usuário com ID '{usuario_id_excluir}' não encontrado.")

def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Biblioteca ---")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Consultar Livros Cadastrados")
    print("4. Consultar Usuários Cadastrados")
    print("5. Consultar Livro por ISBN")
    print("6. Emprestar Livro")
    print("7. Excluir Livro")
    print("8. Excluir Usuário")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    biblioteca = Biblioteca()

    while True:
        opcao = exibir_menu()
        if opcao == '1':
            biblioteca.cadastrar_livro()
        elif opcao == '2':
            biblioteca.cadastrar_usuario()
        elif opcao == '3':
            biblioteca.consultar_livros()
        elif opcao == '4':
            biblioteca.consultar_usuarios()
        elif opcao == '5':
            biblioteca.consultar_livro_por_isbn()
        elif opcao == '6':
            biblioteca.emprestar_livro()
        elif opcao == '7':
            biblioteca.excluir_livro()
        elif opcao == '8':
            biblioteca.excluir_usuario()
        elif opcao == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()