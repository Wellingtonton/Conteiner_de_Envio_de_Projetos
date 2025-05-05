from typing import Dict, List, Optional

# Definindo um tipo para representar um colaborador
Colaborador = Dict[str, any]

def adicionar_colaborador(cadastro: Dict[int, Colaborador], id: int, nome: str, salario: float) -> None:
    """Adiciona um novo colaborador ao cadastro."""
    if id in cadastro:
        print(f"Erro: Colaborador com ID {id} já existe.")
        return
    cadastro[id] = {'nome': nome, 'salario': salario}
    print(f"Colaborador '{nome}' (ID: {id}) adicionado com sucesso.")

def buscar_colaborador_por_id(cadastro: Dict[int, Colaborador], id: int) -> Optional[Colaborador]:
    """Busca um colaborador no cadastro pelo ID."""
    if id in cadastro:
        return cadastro[id]
    else:
        print(f"Colaborador com ID {id} não encontrado.")
        return None

def listar_colaboradores_salario_acima(cadastro: Dict[int, Colaborador], salario_minimo: float) -> List[Colaborador]:
    """Lista os colaboradores com salário acima do valor especificado."""
    colaboradores_filtrados = [
        colaborador for colaborador in cadastro.values() if colaborador['salario'] > salario_minimo
    ]
    if colaboradores_filtrados:
        print(f"\nColaboradores com salário acima de R$ {salario_minimo:.2f}:")
        for colaborador in colaboradores_filtrados:
            print(f"- Nome: {colaborador['nome']}, Salário: R$ {colaborador['salario']:.2f}")
    else:
        print(f"Nenhum colaborador com salário acima de R$ {salario_minimo:.2f} encontrado.")
    return colaboradores_filtrados

def exibir_menu_colaboradores():
    """Exibe o menu de operações com colaboradores."""
    print("\n--- Menu de Colaboradores ---")
    print("1. Adicionar novo colaborador")
    print("2. Buscar colaborador por ID")
    print("3. Listar colaboradores com salário acima de...")
    print("0. Voltar ao menu principal")
    print("-----------------------------\n")

def menu_gerenciamento_colaboradores(cadastro_colaboradores: Dict[int, Colaborador]):
    """Função para o menu de gerenciamento de colaboradores."""
    while True:
        exibir_menu_colaboradores()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            try:
                id = int(input("Digite o ID do novo colaborador: "))
                nome = input("Digite o nome do colaborador: ")
                salario = float(input("Digite o salário do colaborador: "))
                adicionar_colaborador(cadastro_colaboradores, id, nome, salario)
            except ValueError:
                print("Entrada inválida. Certifique-se de digitar um número para ID e salário.")
        elif opcao == '2':
            try:
                id_busca = int(input("Digite o ID do colaborador que deseja buscar: "))
                colaborador = buscar_colaborador_por_id(cadastro_colaboradores, id_busca)
                if colaborador:
                    print(f"\n--- Dados do Colaborador (ID: {id_busca}) ---")
                    print(f"Nome: {colaborador['nome']}")
                    print(f"Salário: R$ {colaborador['salario']:.2f}")
                    print("--------------------------------------------\n")
            except ValueError:
                print("Entrada inválida. Digite um número para o ID.")
        elif opcao == '3':
            try:
                salario_minimo = float(input("Digite o salário mínimo para a listagem: "))
                listar_colaboradores_salario_acima(cadastro_colaboradores, salario_minimo)
            except ValueError:
                print("Entrada inválida. Digite um número para o salário.")
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso (em memória)
cadastro_de_colaboradores = {}

if __name__ == "__main__":
    menu_gerenciamento_colaboradores(cadastro_de_colaboradores)