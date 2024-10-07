#Importar as bibliotecas necessárias
import pandas as pd
import pyautogui
import time


#Iniciando a automação
pyautogui.PAUSE = 1 # Define uma pausa de 1 segundo entre as ações
# abrir o RM TOTVS
pyautogui.press("win")
pyautogui.write("rm")
pyautogui.press("enter")
# entrar no link 

# Pausa a execução por 10 segundos
time.sleep(5) 

# Passo 2: Fazer login
# selecionar o campo de login
pyautogui.click(x=1213, y=441)
# escrever a senha na posição capturada
pyautogui.write("totvs")
pyautogui.press("enter")

# Aguardar o RM abrir
time.sleep(10)

# Navegar até o Menu de Gestão de Compras e Estoque
pyautogui.click(x=18, y=45)
pyautogui.click(x=114, y=202)
pyautogui.click(x=419, y=240)

# Acessando o Menu Contratos
pyautogui.click(x=344, y=49)
pyautogui.click(x=119, y=111)
time.sleep(2)

# Escolhendo o Filtro    981111
pyautogui.doubleClick(x=844, y=353)
pyautogui.click(x=1046, y=773)

# Importar a base de contratos para faturar
tabela = pd.read_csv("contratos.csv")

# Obter o último índice do DataFrame
ultimo_indice = tabela.index[-1]

for linha in tabela.index:
    nome = tabela.loc[linha, "Codigo"]
    # preencher o campo
    pyautogui.write(str(nome))
    pyautogui.click(x=998, y=641)

    #Fatura o Contrato
    pyautogui.click(x=48, y=338)
    pyautogui.click(x=601, y=196)
    pyautogui.click(x=685, y=287)
    pyautogui.click(x=1057, y=716)

    # Aguardar o RM abrir
    time.sleep(10)

    #clicar em Fechar a Tela de Faturamento
    pyautogui.click(x=1154, y=719)

    if linha == ultimo_indice:
        # Executar as funções adicionais para o último registro
        print("Este é o último registro!")
        print("Processo terminado")
        break  # Para a execução do loop aqui, sem filtrar o próximo contrato

    # filtrar o próximo contrato
    pyautogui.click(x=750, y=196)
    # Apagando o filtro anterior
    pyautogui.press('delete')

  
