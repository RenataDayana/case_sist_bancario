class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        tentativa=0
        while tentativa < 2:
            if valor>0:
                self.saldo += valor
                print(f'Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}')
                return
            else:
                print("O valor para depósito deve ser positivo.")
                tentativa += 1
                if tentativa < 2:  
                    valor = ContaBancaria.obter_valor_input('Informe um valor válido para depósito: R$')
    
        print("Número máximo de tentativas excedido. Depósito não realizado.")
    def sacar(self, valor):
        if valor>0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}')
            else:
                print('Saldo insuficiente para saque.')
        else:
            print("\nSaque não realizado. O valor de saque deve ser positivo. ")

    def transferir(self, destinatario, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                destinatario.depositar(valor)
                print(f'Transferência de R${valor:.2f} realizada. Novo saldo conta: R${self.saldo:.2f}')
            else:
                print('Saldo insuficiente para transferência.')
        else:
            print('Transferência não realizada. O valor para transferência deve ser positivo.')

    @staticmethod
    def obter_valor_input(mensagem):
        while True:
            try:
                valor = float(input(mensagem))   
                if valor<0:
                    print('O valor deve ser positivo.')   
                else:          
                    return valor
            except ValueError:
                print('Por favor, insira um valor numérico válido.')
def main():
    print("Bem vindo(a)!")
    conta1_saldo_inicial = ContaBancaria.obter_valor_input('\nInforme o saldo inicial da conta 1: R$')
    conta2_saldo_inicial = ContaBancaria.obter_valor_input('Informe o saldo inicial da conta 2: R$')

    conta1 = ContaBancaria(conta1_saldo_inicial)
    conta2 = ContaBancaria(conta2_saldo_inicial)

    while True:
        print('\nOpções:')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Transferir')
        print('4. Consultar Saldo')
        print('5. Sair')

        escolha = input('\nEscolha uma opção (1-5): ')
        if escolha == '1':
            conta = input('Escolha a conta para depósito: ')
            if conta =='1':
                valor_deposito = ContaBancaria.obter_valor_input('Informe o valor a ser depositado na Conta 1: R$')
                conta1.depositar(valor_deposito)
            elif conta =='2':
                valor_deposito = ContaBancaria.obter_valor_input('Informe o valor a ser depositado na Conta 2: R$')
                conta2.depositar(valor_deposito)
            else:
                print('Conta inválida. Tente novamente.')
        elif escolha == '2':
            conta = input('Escolha a conta para saque: ')
            if conta == '1':
                valor_saque = ContaBancaria.obter_valor_input('Informe o valor a ser sacado da Conta 1: R$')
                conta1.sacar(valor_saque)
            elif conta == '2':
                valor_saque = ContaBancaria.obter_valor_input('Informe o valor a ser sacado da Conta 2: R$')
                conta2.sacar(valor_saque)
            else:
                print('Conta inválida. Tente novamente.')
        elif escolha == '3':
            valor_transferencia = ContaBancaria.obter_valor_input('Informe o valor a ser transferido: R$')
            conta_origem = input('Escolha a conta de origem: ')
            conta_destino = input('Escolha a conta de destino: ')

            if conta_origem == '1' and conta_destino == '2':
                conta1.transferir(conta2, valor_transferencia)
            elif conta_origem == '2' and conta_destino =='1':
                conta2.transferir(conta1, valor_transferencia)
            else:
                print('Conta inválida para transferência. Tente novamente.')
        elif escolha == '4':       
            print(f'\nSaldo conta 1: R${conta1.saldo:.2f}')
            print(f'Saldo conta 2: R${conta2.saldo:.2f}')
        elif escolha == '5':
            break
        else:
            print('Opção inválida. Tente uma das opções disponíveis.')

    print('\nSaldos Finais:')
    print(f'Conta 1: R${conta1.saldo:.2f}')
    print(f'Conta 2: R${conta2.saldo:.2f}')

if __name__ == "__main__":
    main()