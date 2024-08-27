import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

# Obtendo dados da base de dados do Excel
dados = pd.read_excel(r"C:\Users\PESSOAL\Desktop\AutoEscala\CodFontAutoEscala\Escala_Processada.xlsx")

# Obtendo apenas as colunas (Funcao e Nome)
Funcoes = dados['Funcao']
Nomes = dados['Nome']
lista_nome = []
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

# Função para identificar sequências contínuas com ajuste para tratar o período do dia 16 até o dia 15 como uma única sequência contínua
def identificar_sequencias(colunas_vazias):

    sequencias = []
    sequencia_atual = []

    for i in range(len(colunas_vazias)):
        dia_atual = int(colunas_vazias[i])
        dia_anterior = int(colunas_vazias[i - 1]) if i > 0 else None

        # Ajuste para continuidade no ciclo de 16 a 15
        if dia_anterior is not None and (
            dia_atual == dia_anterior + 1 or (dia_anterior == 30 and dia_atual == 1)
        ):
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
    global lista_nome

    for index, row in dados.iterrows():
        nome = row['Nome']

        if pd.notna(nome):  # Verifica se o nome não é NaN
            colunas_vazias = []
            # Iterar sobre as colunas específicas (da coluna 16 até a 15)
            for i in range(colunas.index("16"), colunas.index("15") + 1):
                coluna_nome = colunas[i]  # Nome da coluna
                coluna_valor = row[coluna_nome]  # Valor da célula correspondente

                if pd.notna(coluna_valor) and any(term in str(coluna_valor).upper() for term in termos):
                    colunas_vazias.append(coluna_nome)  # Adicionar à lista se o valor está na lista de exclusão
                    # Pular para a próxima iteração se o valor está na lista de exclusão
                elif pd.isna(coluna_valor):
                    colunas_vazias.append(coluna_nome)  # Se a coluna está vazia, adicioná-la à lista

            # Identificar as sequências contínuas de colunas vazias
            sequencias = identificar_sequencias(colunas_vazias)
            multiplas_sequencias = [seq for seq in sequencias if len(seq) > 1]

            # Se houver múltiplas sequências, imprimir
            if multiplas_sequencias:
                print(f"{nome}: Dias indisponível - {multiplas_sequencias}")

            # Imprimir os dias disponíveis, que são os que não fazem parte de uma sequência
            dias_disponiveis = [dia for dia in colunas_vazias if
                                dia not in [item for sublist in multiplas_sequencias for item in sublist]]
            if dias_disponiveis:
                print(f"{nome}: Dias disponíveis: {dias_disponiveis}")
                lista_nome.append(nome)


# Executar a função
processar_dados(dados, termos)

print("\n Nomes disponiveis")
for nome in (lista_nome):
    print(nome)

#Whatsapp
driver = webdriver.Chrome()  #Drive do navegador

driver.get("https://web.whatsapp.com/") # Acessando o whatsap

time.sleep(15) # 20 Segundos para ler o Código QR

def pesquisa_barra(browser, nome_grupo):
    barra_pesquisa = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')))
    barra_pesquisa.click()

    print("Cliquei no campo de busca de contato")
    time.sleep(5)

    barra_pesquisa.send_keys(nome_grupo)
    print("Digitei")
    time.sleep(6)


    barra_pesquisa.send_keys(Keys.ENTER)
    print("Apertei ENTER")
    time.sleep(7)

# Enviando mensagem

def enviando_mensagem(browser, mensagem_grupo):
    barra_mensagem = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
    barra_mensagem.click()

    time.sleep(5)

    barra_mensagem.send_keys(mensagem_grupo)
    time.sleep(6)

    barra_mensagem.send_keys(Keys.ENTER)
    time.sleep(7)

mensagem_cabecalho = """\Olá, pessoal! Sou um robô super simpático aqui para ajudar com a escala de folgas. Por favor, preencham o dia que desejam folgar, seguindo o exemplo abaixo:

Exemplo: Juriscreide Nascimento Bezerra - dia 28

Agora é a vez de vocês:
"""


# Combina o cabeçalho com a lista de nomes
mensagem_completa = mensagem_cabecalho + "\n".join(lista_nome)

# Cria um DataFrame com a mensagem completa, linha por linha
df = pd.DataFrame({"Mensagem": [mensagem_completa]})

# Salva o DataFrame em um arquivo Excel
df.to_excel("mensagem_completa.xlsx", index=False)

# 2. Ler a mensagem do Excel
df_lido = pd.read_excel("mensagem_completa.xlsx")
mensagem_grupo = df_lido["Mensagem"].iloc[0]  # Pega o primeiro e único item

print("Mensagem salva com sucesso em 'mensagem_completa.xlsx'")

pesquisa_barra(driver, "Grupo da Enfermagem")


enviando_mensagem(driver, mensagem_grupo)

time.sleep(20)  # Aguarda 5 segundos para visualizar o resultado
driver.quit()
