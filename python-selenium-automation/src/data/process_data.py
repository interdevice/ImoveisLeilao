import chardet
import pandas as pd
import csv

def create_dataframe(file_path):
    dados = []
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())

    encoding = result['encoding']

    with open(file_path, 'r', encoding=encoding) as file:
        leitor = csv.reader(file)
        for linha in leitor:
            dados.append(linha)

    # Encontra o número máximo de colunas
    max_cols = max(len(linha) for linha in dados)

    # Completa as linhas com valores vazios para ter o mesmo número de colunas
    for linha in dados:
        while len(linha) < max_cols:
            linha.append('')  # Ou outro valor que represente um campo vazio

    # Cria o DataFrame
    df = pd.DataFrame(dados)
    return df