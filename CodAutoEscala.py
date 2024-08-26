import pandas as pd

# Obtendo dados da base de dados do Excel
dados = pd.read_excel(r"C:\Users\PESSOAL\Desktop\AutoEscala\CodFontAutoEscala\Escala_Processada.xlsx")

# Obtendo apenas as colunas (Funcao e Nome)
Funcoes = dados['Funcao']
Nomes = dados['Nome']

# Lista de termos de exclusão
termos = [
    'AFASTAMENTO DO INSS', 'LN', 'LINCENÇA NOJO', 'FC', 'FOLGA CATEGORIA',
    'LM', 'LICENÇA MATERNIDADE', 'AF', 'AFASTAMENTO', 'G', 'GESTAÇÃO',
    'TR', 'TREINAMENTO', 'FE', 'FÉRIAS'
]

# Listando todas as colunas
colunas = list(dados.columns)

# Localiza o índice da coluna chamada '16' e da coluna '15'
indice_coluna_16 = colunas.index("16")
ultimo_indice = colunas.index("15")


# Função para identificar sequências contínuas
def identificar_sequencias(colunas_vazias):
    sequencias = []
    sequencia_atual = []

    for i in range(len(colunas_vazias)):
        if i == 0 or int(colunas_vazias[i]) == int(colunas_vazias[i - 1]) + 1:
            sequencia_atual.append(colunas_vazias[i])
        else:
            if sequencia_atual:
                sequencias.append(sequencia_atual)
            sequencia_atual = [colunas_vazias[i]]

    if sequencia_atual:
        sequencias.append(sequencia_atual)

    return sequencias


# Função principal para processar os dados
def processar_dados(dados, termos):
    for index, row in dados.iterrows():
        nome = row['Nome']

        if pd.notna(nome):  # Verifica se o nome não é NaN
            colunas_vazias = []

            # Iterar sobre as colunas específicas (da coluna 16 até a 15)
            for i in range(colunas.index("16"), colunas.index("15") + 1):
                coluna_nome = colunas[i]  # Nome da coluna
                coluna_valor = row[coluna_nome]  # Valor da célula correspondente

                if pd.notna(coluna_valor) and any(term in str(coluna_valor).upper() for term in termos):
                    continue  # Pular para a próxima iteração se o valor está na lista de exclusão
                elif pd.isna(coluna_valor):
                    colunas_vazias.append(coluna_nome)  # Se a coluna está vazia, adicioná-la à lista

            # Identificar as sequências contínuas de colunas vazias
            sequencias = identificar_sequencias(colunas_vazias)
            multiplas_sequencias = [seq for seq in sequencias if len(seq) > 1]

            # Se houver múltiplas sequências, imprimir
            if multiplas_sequencias:
                print(f"{nome}: Múltiplas sequências de colunas vazias - {multiplas_sequencias}")

            # Imprimir os dias disponíveis, que são os que não fazem parte de uma sequência
            dias_disponiveis = [dia for dia in colunas_vazias if
                                dia not in [item for sublist in multiplas_sequencias for item in sublist]]
            if dias_disponiveis:
                print(f"{nome}: Dias disponíveis (sem sequências): {dias_disponiveis}")


# Executar a função
processar_dados(dados, termos)
