from banco import Cliente, ContaCorrente
from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError

# Testando erros e tratamentos 
conta_corrente1 = ContaCorrente(None, 1234, 125)
conta_corrente2 = ContaCorrente(None, 124, 126)
try:
    conta_corrente1.sacar(1000)
except OperacaoFinanceiraError as E:
    raise