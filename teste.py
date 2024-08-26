import pandas as pd

#Ler a base de dados
base_dados = pd.read_excel(r"C:\Users\PESSOAL\Desktop\AutoEscala\CodFontAutoEscala\Escala_Processada.xlsx")

# Identificar a coluna Nome
coluna_Nome = base_dados[['Nome']]

# Remover linhas sem dados da coluna nome
for index, row in base_dados.iterrows():
    coluna_Nomes = row['Nome']
    if pd.notna(coluna_Nomes):
        Coluna_Nomes = row['Nome']

# Identificar as colunas 16 até a coluna 15
        colunas = list(base_dados.columns)
        for i in range(colunas.index("16"), colunas.index("15") + 1):  # Ajuste o range conforme necessário
            coluna_nome = colunas[i]  # Nome da coluna
            coluna_valor = row[coluna_nome]  # Valor da célula correspondente

# Verificar se contem mais de uma coluna de uma lista vazia em sequencia ou com mais de uma string dentro

# Na coluna Nome ler do primeio ao ultimo nome da lista e quais dados das colunas 16 ate a 15


# SE houver, contar incluindo a coluna que contem mais de uma string dentro

# Parar de contar quando indentificar uma unica string dentro de uma coluna podendo ser D ou F

# Depos da string D ou F retornar o numero da coluna que estiver vazia, entre 16 ate a 15

# Retornar os Nomes da coluna nome e os nomes das colunas que estão vazias apos D ou F dentro do numero 16 até o 15

# Criar uma mensagem com os nomes e os numeros das colunas

#A#####
import pandas as pd

# Carrega os dados do Excel
dados = pd.read_excel(r"C:\Users\PESSOAL\Desktop\AutoEscala\CodFontAutoEscala\Escala_Processada.xlsx")


# Função para identificar sequências contínuas de colunas vazias
def identificar_sequencias(colunas_vazias):
    sequencias = []
    seq_atual = []

    for i, coluna in enumerate(colunas_vazias):
        if i == 0 or int(coluna) == int(colunas_vazias[i - 1]) + 1:
            seq_atual.append(coluna)
        else:
            if len(seq_atual) > 1:  # Só adiciona sequências de mais de um dia
                sequencias.append(seq_atual)
            seq_atual = [coluna]

    if len(seq_atual) > 1:  # Adiciona a última sequência se for maior que 1 dia
        sequencias.append(seq_atual)

    return sequencias


# Processa cada linha (funcionário)
for index, row in dados.iterrows():
    nome = row['Nome']

    if pd.notna(nome):  # Verifica se o nome não é NaN
        colunas_vazias = []

        # Itera sobre as colunas "16" até "15"
        for i in range(dados.columns.get_loc("16"), dados.columns.get_loc("15") + 1):
            coluna_nome = dados.columns[i]
            coluna_valor = row[coluna_nome]

            if pd.isna(coluna_valor):
                colunas_vazias.append(coluna_nome)

        # Identifica as sequências contínuas
        sequencias_vazias = identificar_sequencias(colunas_vazias)

        # Verifica se há mais de uma sequência de colunas vazias
        if len(sequencias_vazias) > 0:  # Agora só imprime se houver sequências com mais de um dia consecutivo
            print(f"{nome}: Múltiplas sequências de colunas vazias - {sequencias_vazias}")

