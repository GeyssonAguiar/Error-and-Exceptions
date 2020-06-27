from leitor import LeitorDeArquivo

# Fechando o arquivo independente de erros 


# Com finally
""" try:
    leitor = LeitorDeArquivo('arquivo.txt')
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
finally:
    if 'leitor' in locals():
        leitor.fechar()  """

# Com with
with LeitorDeArquivo('arquivo.txt') as leitor:
    leitor.ler_proxima_linha()
