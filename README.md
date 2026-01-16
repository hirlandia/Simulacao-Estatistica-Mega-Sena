# 🎲 Análise Estatística da Mega-Sena: De Dados Brutos a Insights Visuais

Neste projeto, desenvolvi um script em Python que analisa o histórico de sorteios da Mega-Sena. A proposta foi aplicar técnicas de **Data Analytics** para transformar um arquivo CSV com milhares de registros em informações visuais compreensíveis, identificando padrões de frequência e gerando simulações baseadas em dados reais.

O sistema funciona via terminal (CLI) e culmina na geração de um gráfico estatístico que apresenta os números mais sorteados em toda a história da loteria.

## 💡 O Desafio
O maior desafio foi a **limpeza e tratamento dos dados**. Arquivos de resultados históricos costumam vir com cabeçalhos informativos e formatação que impedem a leitura direta por bibliotecas de análise. Precisei estruturar o código para saltar linhas irrelevantes, definir colunas manualmente e tratar a matriz de dezenas para que o cálculo de frequência fosse preciso e performático.

## 🔍 O que eu aprendi e apliquei

### Manipulação e Limpeza com Pandas
Aprendi a utilizar o **Pandas** para ir além da leitura simples de tabelas, explorando:
* **Tratamento de Arquivos:** Uso de "skiprows" e "encoding="latin-1"" para lidar com arquivos CSV fora do padrão.
* **Data Shaping:** Transformação de múltiplas colunas de dezenas em uma única série de dados usando "flatten()" e "value_counts()".

### Probabilidade e Sorteio Ponderado
Diferente de um sorteio aleatório comum, utilizei a lógica de **pesos estatísticos**:
* Implementação da função "random.choices" utilizando a frequência histórica como peso ("weights").
* Isso garante que a simulação de jogo "respeite" a tendência dos números que mais (ou menos) aparecem no banco de dados.

### Visualização de Dados (Matplotlib)
Trabalhei com a **Matplotlib** para transformar números em impacto visual:
* Criação de gráficos de barras para o **Top 10** números mais frequentes.
* Customização de layout, títulos e eixos.
* Inclusão de anotações dinâmicas (texto do jogo sugerido) dentro da figura do gráfico.
<img width="1120" height="627" alt="image" src="https://github.com/user-attachments/assets/921727a6-aa15-497b-96f6-c6bd2519920b" />

### Estruturação de Projeto
Mantive o foco em **Clean Code** e modularização:
* "funcoes.py": Camada de lógica, processamento de dados e cálculos.
* "main.py": Camada de interface, interação com o usuário e exibição de resultados.

## 🛠️ Tecnologias e Bibliotecas
* **Python 3**
* **Pandas**: Manipulação e análise de dados.
* **Matplotlib**: Visualização de dados e gráficos.
* **OS & Random**: Gerenciamento de caminhos de arquivos e lógica probabilística.

## 🚀 Como executar o projeto

1. **Clone o repositório:**
(https://github.com/hirlandia/Simulacao-Estatistica-Mega-Sena.git)

2. **Instale as dependências:**
Bash
    pip install pandas matplotlib
   
</br>
* 🖥️ DADOS RETIRADOS
</br>As Loterias - www.asloterias.com.br - Todos Resultados da Mega Sena
</br>Este arquivo foi baixado no site www.asloterias.com.br no dia 15/01/2026
</br>Visite o site para baixar a versão mais atualizada deste arquivo!

</br>TODOS RESULTADOS DA MEGA SENA POR ORDEM DE SORTEIO


