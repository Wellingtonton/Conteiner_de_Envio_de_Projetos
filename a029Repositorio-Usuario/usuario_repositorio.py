from typing import List, Dict, Optional
from email_validator import validate_email, EmailNotValidError


class UsuarioNaoEncontrado(Exception):
    """Exceção personalizada para quando o usuário não for encontrado."""
    pass


# METACLASSE: Garante que os métodos essenciais existem no repositório
class RepositoryMeta(type):
    def __new__(mcs, name, bases, dct):
        required_methods = [
            'cadastrar',
            'listar_todos',
            'buscar_por_email',
            'remover',
            'atualizar_email',
            'listar_por_nome',
            'listar_por_email',
            'listar_por_nome_e_email'
        ]
        for method in required_methods:
            if method not in dct:
                raise TypeError(f"A classe {name} deve implementar o método '{method}'")
        return super().__new__(mcs, name, bases, dct)


# Aplicação da metaclasse no repositório
class UsuarioRepository(metaclass=RepositoryMeta):
    def __init__(self):
        self._usuarios: List[Dict[str, str]] = []

    def cadastrar(self, usuario: Dict[str, str]) -> None:
        if not self._validar_usuario(usuario):
            raise ValueError("Usuário deve conter nome e email válidos.")
        if self.buscar_por_email(usuario['email']):
            raise ValueError(f"Já existe um usuário cadastrado com o email {usuario['email']}")
        self._usuarios.append(usuario.copy())

    def listar_todos(self) -> List[Dict[str, str]]:
        return self._usuarios.copy()

    def buscar_por_email(self, email: str) -> Optional[Dict[str, str]]:
        return next((usuario for usuario in self._usuarios if usuario['email'] == email), None)

    def remover(self, email: str) -> bool:
        usuario = self.buscar_por_email(email)
        if not usuario:
            raise UsuarioNaoEncontrado(f"Usuário com email {email} não encontrado.")
        self._usuarios.remove(usuario)
        return True

    def atualizar_email(self, email_atual: str, nome: str, novo_email: str) -> bool:
        for i, usuario in enumerate(self._usuarios):
            if usuario['email'] == email_atual and usuario['nome'].lower() == nome.lower():
                try:
                    validate_email(novo_email)
                except EmailNotValidError as e:
                    raise ValueError(f"Novo email inválido: {e}")

                if self.buscar_por_email(novo_email):
                    raise ValueError("Já existe um usuário com esse novo email.")

                self._usuarios[i]['email'] = novo_email
                return True
        raise UsuarioNaoEncontrado("Nome e email não conferem.")

    def listar_por_nome(self, nome: str) -> List[Dict[str, str]]:
        return [usuario for usuario in self._usuarios if usuario['nome'] == nome]

    def listar_por_email(self, email: str) -> List[Dict[str, str]]:
        return [usuario for usuario in self._usuarios if usuario['email'] == email]

    def listar_por_nome_e_email(self, nome: str, email: str) -> List[Dict[str, str]]:
        return [usuario for usuario in self._usuarios if usuario['nome'] == nome and usuario['email'] == email]

    def _validar_usuario(self, usuario: Dict[str, str]) -> bool:
        nome_valido = 'nome' in usuario and isinstance(usuario['nome'], str) and usuario['nome'].strip() != ''
        email_valido = False
        if 'email' in usuario and isinstance(usuario['email'], str):
            try:
                validate_email(usuario['email'])
                email_valido = True
            except EmailNotValidError:
                email_valido = False
        return nome_valido and email_valido


# Funções auxiliares (sem alteração)
def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Cadastrar novo usuário")
    print("2. Listar todos os usuários")
    print("3. Buscar usuário por email")
    print("4. Remover usuário por email")
    print("5. Atualizar email do usuário")
    print("6. Listar usuários por nome")
    print("7. Listar usuários por email")
    print("8. Listar usuários por nome e email")
    print("9. Sair")


def executar_comando(repo: UsuarioRepository):
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            try:
                repo.cadastrar({'nome': nome, 'email': email})
                print(f"Usuário {nome} cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro ao cadastrar: {e}")

        elif opcao == '2':
            usuarios = repo.listar_todos()
            print(f"Todos os usuários: {usuarios}")

        elif opcao == '3':
            email = input("Digite o email para buscar: ")
            usuario = repo.buscar_por_email(email)
            if usuario:
                print(f"Usuário encontrado: {usuario}")
            else:
                print("Usuário não encontrado!")

        elif opcao == '4':
            email = input("Digite o email do usuário a ser removido: ")
            try:
                repo.remover(email)
                print(f"Usuário com email {email} removido com sucesso!")
            except UsuarioNaoEncontrado as e:
                print(f"Erro ao remover usuário: {e}")

        elif opcao == '5':
            email_atual = input("Digite seu email atual: ")
            nome = input("Digite seu nome completo: ")
            novo_email = input("Digite o novo email: ")
            try:
                repo.atualizar_email(email_atual, nome, novo_email)
                print("Email atualizado com sucesso!")
            except (UsuarioNaoEncontrado, ValueError) as e:
                print(f"Erro ao atualizar email: {e}")

        elif opcao == '6':
            nome = input("Digite o nome para listar os usuários: ")
            usuarios = repo.listar_por_nome(nome)
            print(f"Usuários encontrados com o nome {nome}: {usuarios}")

        elif opcao == '7':
            email = input("Digite o email para listar os usuários: ")
            usuarios = repo.listar_por_email(email)
            print(f"Usuários encontrados com o email {email}: {usuarios}")

        elif opcao == '8':
            nome = input("Digite o nome para listar os usuários: ")
            email = input("Digite o email para listar os usuários: ")
            usuarios = repo.listar_por_nome_e_email(nome, email)
            print(f"Usuários encontrados com o nome {nome} e email {email}: {usuarios}")

        elif opcao == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    repo = UsuarioRepository()
    executar_comando(repo)
