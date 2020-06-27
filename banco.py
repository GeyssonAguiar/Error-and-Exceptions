from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    # ATRIBUTOS DE CLASSE
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        # ATRIBUTOS DE INSTÂNCIA
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidos = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    #
    # Encapsulando os atributos
    #

    @property
    def agencia(self):
        return self.__agencia

    # setter agencia
    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo agencia deve ser inteiro', value)
        if value <= 0:
            raise ValueError('O atributo agencia deve ser maior que 0', value)
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):

        if not isinstance(value, int):
            # Utilizando raise para lançar Erro
            raise ValueError('O atributo numero deve ser inteiro')
        if value <= 0:
            # Utilizando raise para lançar Erro
            raise ValueError('O atributo numero deve ser maior que 0')
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            # Utilizando raise para lançar Erro
            raise ValueError('O atributo saldo deve ser inteiro')

        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            # Utilizando raise para lançar Erro
            raise ValueError('O valor a ser transferido não pode ser \
                menor que 0')
        try:
            self.sacar(valor)
        # Modificando tratamento de SaldoInsuficienteError
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidos += 1
            E.args = ()
            raise OperacaoFinanceiraError('Operação não finalizada') from E

        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            # Utilizando raise para lançar Erro
            raise ValueError('O valor a ser sacado não pode ser menor que 0')
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
             # Utilizando raise para lançar Erro
            raise SaldoInsuficienteError('', self.saldo, valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor





