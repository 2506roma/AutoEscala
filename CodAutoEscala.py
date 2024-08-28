import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib
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
mensagem_cabecalho = """\Olá, pessoal! Sou um robô super simpático aqui para ajudar com a escala de folgas. Por favor, preencham o dia que desejam folgar, seguindo o exemplo abaixo:

Exemplo: Juriscreide Nascimento Bezerra - dia 28

Agora é a vez de vocês:
"""

#Whatsapp
driver = webdriver.Chrome()  #Drive do navegador

def enviando_mensagem(browser, mensagem_link):

    driver.get(f"https://web.whatsapp.com/send?phone={5511983352507}&text={mensagem_nova}") #Acessando whatsapp
    time.sleep(15) # 20 Segundos para ler o Código QR


    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')))
    enviando_msg_contato.click()

    time.sleep(5)

    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')))
    enviando_msg_contato.click()

    time.sleep(5)

    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/div/li[2]/div')))
    enviando_msg_contato.click()

    time.sleep(10)
    
    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[13]/div/div/span/div/div')))
    enviando_msg_contato.click()

    time.sleep(8)

    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/span[2]/div/button[4]/span')))
    enviando_msg_contato.click()

    time.sleep(5)

    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p')))
    enviando_msg_contato.click()


    time.sleep(5)
    #COLANDO O NOME
    nome_grupo = "Grupo da Enfermagem"
    enviando_msg_contato.send_keys(nome_grupo)
    time.sleep(7)

    #Selecionando o Grupo
    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div')))
    enviando_msg_contato.click()

    enviando_msg_contato = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span')))
    enviando_msg_contato.click()

    time.sleep(3)
    #enviando_msg_contato.send_keys(Keys.ENTER)


    #barra_pesquisa.send_keys(Keys.ENTER)


# Enviando mensagem

#Teste
def construir_mensagem(cabecalho, nomes):
    """Constrói a mensagem completa combinando o cabeçalho com a lista de nomes."""
    mensagem = cabecalho
    for nome in nomes:
        mensagem += f"{nome}\n"  # Adiciona cada nome seguido por uma quebra de linha
    return mensagem
#Teste

mensagem_nova = construir_mensagem(mensagem_cabecalho, lista_nome)

print("Nomes pronto")
time.sleep(5)
# Combina o cabeçalho com a lista de nomes
mensagem_completa = str(mensagem_cabecalho) + str(lista_nome)
mensagem_nova = urllib.parse.quote(mensagem_nova)
# Cria um DataFrame com a mensagem completa, linha por linha
df = pd.DataFrame({"Mensagem": [mensagem_completa]})

# Salva o DataFrame em um arquivo Excel
df.to_excel("mensagem_completa.xlsx", index=False)
print("Mensagem salva com sucesso em 'mensagem_completa.xlsx'")

# 2. Ler a mensagem do Excel
df_lido = pd.read_excel("mensagem_completa.xlsx")
mensagem_grupo = df_lido["Mensagem"].iloc[0]  # Pega o primeiro e único item
print("Documento pronto")
time.sleep(5)
print(mensagem_grupo)

enviando_mensagem(driver, mensagem_nova)



time.sleep(20)  # Aguarda 5 segundos para visualizar o resultado
driver.quit()
