class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, message='',saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor 
        msg = 'Saldo insuficiente para efetuar a transação' \
            f' Saldo atual: {self.saldo} valor a ser sacado: {self.valor}'
        self.msg = (message or msg) 
        super().__init__(self.msg, self.saldo, self.valor, *args)