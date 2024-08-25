import pandas as pd #inportando biblioteca pandas, abreviando pandas para pd
from numpy.ma.core import append

#Obtendo dados da base de dados do excel
dados = pd.read_excel(r"C:\Users\PESSOAL\Desktop\AutoEscala\CodFontAutoEscala\Escala_Processada.xlsx")

#Obtendo apenas as colunas (Funcao e Nome)
nome_funcao = dados[['Funcao', 'Nome']]
Funcoes = dados['Funcao']
Nomes = dados['Nome']

lista_funcionarios = [ ]
# Lista de exclusão
termos = ['AFASTAMENTO DO INSS','LN','LINCENÇA NOJO','FC','FOLGA CATEGORIA','LM','LICENÇA MATERNIDADE','AF','AFASTAMENTO','G','GESTAÇÃO','TR','TREINAMENTO','FE','FÉRIAS']



# Listando todas as colunas
colunas = list(dados.columns)

# Localiza o índice da coluna chamada '16'
indice_coluna_16 = colunas.index("16")

#Localizando o ultimo indice da coluna '15'
ultimo_indice = colunas.index("15")
# Contar as colunas da "16" até a última
total_colunas = len(colunas[indice_coluna_16:])



for index, row in dados.iterrows():
    nome = row['Nome']

    if pd.notna(nome):  # Verifica se o nome não é NaN
        colunas_vazias = []
        nome = row['Nome']

        # Iterar sobre as colunas específicas (a partir da coluna 16 até a 15)
        for i in range(colunas.index("16"), colunas.index("15") + 1):  # Ajuste o range conforme necessário


            coluna_nome = colunas[i] # Nome da coluna
            coluna_valor = row[coluna_nome]  # Valor da célula correspondente

            if pd.notna(coluna_valor) and coluna_valor in termos:
                # Se o valor da coluna está na lista de termos de exclusão
                continue  # Pular para a próxima iteração (ou faça algo aqui)
            elif pd.isna(coluna_valor):
                # Se a coluna está vazia
                colunas_vazias.append(coluna_nome)

        # Imprimir ou armazenar o resultado
        print(f"{nome}: Colunas vazias - {colunas_vazias}")

#for Funcao, Nome in zip(Funcoes, Nomes):
    # Indentificando se as duas listas está com dados ou vazio
    #if pd.isna(Funcao) or pd.isna(Nome):#pd.isna retorna TRUE se o valor for NaN ou vazio
        #print(" ")
    #else:
        # Adicionando a função e nome na lista_funcionarios
        #lista_funcionarios.append(f"{Funcao} {Nome}")

#for funcionarios in lista_funcionarios:
    #print(funcionarios)

