import pandas as pd
import os
import random

# função para carregar o arquivo csv
def carregar_dados():
    # pega a pasta onde este arquivo está
    pasta_atual = os.path.dirname(__file__)

    # monta o caminho até o csv
    caminho_csv = os.path.join(
        pasta_atual,
        "..",
        "Dados",
        "dados_mega_sena.csv"
    )

    # esse arquivo tem algumas linhas de texto antes da tabela
    # por isso usamos skiprows
    df = pd.read_csv(
        caminho_csv,
        encoding="latin-1",
        sep=",",
        skiprows=6,
        header=None
    )

    # colocando nomes nas colunas
    df.columns = [
        "concurso",
        "data",
        "dezena_1",
        "dezena_2",
        "dezena_3",
        "dezena_4",
        "dezena_5",
        "dezena_6"
    ]
    return df

# função para calcular quantas vezes cada número apareceu
def calcular_frequencia(df):
    # selecionando apenas as colunas das dezenas
    dezenas = df[
        [
            "dezena_1",
            "dezena_2",
            "dezena_3",
            "dezena_4",
            "dezena_5",
            "dezena_6"
        ]
    ]

    # juntando tudo em uma lista só
    numeros = dezenas.values.flatten()
    # contando a frequência
    frequencia = pd.Series(numeros).value_counts().sort_index()
    return frequencia

# função para gerar um jogo baseado na frequência
def sortear_numeros(frequencia):
    numeros = frequencia.index.tolist()
    pesos = frequencia.values.tolist()
    jogo = []
    
    # enquanto não tiver 6 números, continua sorteando
    while len(jogo) < 6:
        numero = random.choices(numeros, weights=pesos, k=1)[0]

        # evita número repetido
        if numero not in jogo:
            jogo.append(numero)

    return sorted(jogo)