class Conta:
    """
    Classe que representa uma conta bancária com controle de saldo.
    """

    def __init__(self, saldo_inicial=0.0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self._saldo = float(saldo_inicial)

    @property
    def saldo(self):
        return f'R${self._saldo:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = float(valor)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor


def menu():
    print("\n=== MENU CONTA BANCÁRIA ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")


if __name__ == "__main__":
    conta = Conta(1000.0)
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Saldo atual:", conta.saldo)

        elif opcao == '2':
            try:
                valor = float(input("Valor do depósito: ").replace(',', '.'))
                conta.depositar(valor)
                print("Depósito realizado com sucesso!")
            except ValueError as e:
                print("Erro:", e)

        elif opcao == '3':
            try:
                valor = float(input("Valor do saque: ").replace(',', '.'))
                conta.sacar(valor)
                print("Saque realizado com sucesso!")
            except ValueError as e:
                print("Erro:", e)

        elif opcao == '4':
            print("Saindo... Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")
