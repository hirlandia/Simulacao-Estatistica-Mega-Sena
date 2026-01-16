from funcoes import carregar_dados, calcular_frequencia, sortear_numeros
import matplotlib.pyplot as plt


def main():
    print("---------------------------------")
    print("   ANÁLISE SIMPLES DA MEGA-SENA   ")
    print("   DESENVOLVIDA POR HIRLANDIA   👩🏽‍💻")
    print("---------------------------------\n")

    nome = input("Digite seu nome: ")

    print(f"\nOlá, {nome}! Seja bem-vindo(a) 🎲")
    print("Vamos simular os dados da Mega-Sena.\n")

    # carregando os dados
    df = carregar_dados()

    print("Arquivo carregado com sucesso!")
    print("Primeiras linhas do arquivo:\n")
    print(df.head())

    # calculando a frequência
    frequencia = calcular_frequencia(df)

    print("\n-----------------------------------")
    print("Números que mais apareceram:")
    print("-----------------------------------")

    top_10 = frequencia.sort_values(ascending=False).head(10)

    posicao = 1
    for numero, qtd in top_10.items():
        print(f"{posicao}º lugar - Número {numero} apareceu {qtd} vezes")
        posicao += 1

    # gerando um jogo sugerido
    jogo = sortear_numeros(frequencia)

    print("\n-----------------------------------")
    print(f"{nome}, com base nos dados históricos:")
    print("Jogo sugerido (simulação): ⌨️")
    print(jogo)
    print("-----------------------------------")

    print("\n- OBSERVAÇÃO: ESTE RESULTADO NÃO É UMA PREVISÃO REAL -")

#MATPLOTLIB

    plt.figure(figsize=(9, 5))

    plt.bar(
        top_10.index.astype(str),
        top_10.values
    )

    plt.title("Histograma dos 10 números mais sorteados")
    plt.xlabel("Número")
    plt.ylabel("Quantidade de vezes sorteado")

    # texto que mostra abaixo do gráfico
    texto_jogo = "Jogo sugerido (simulação): ⌨️ " + " - ".join(map(str, jogo))

    plt.text(
        0.5,
        -0.25,
        texto_jogo,
        ha="center",
        transform=plt.gca().transAxes
    )

    plt.tight_layout()
    plt.show()

main()