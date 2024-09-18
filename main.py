import pandas as pd
from Login import Login
from navegacao import *
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

f = Formatacao()
login = Login()
cnpj = str(login.get_cnpj())
senha = str(login.get_senha())
browser = webdriver.Chrome()
browser.maximize_window()

lerPlanilha = pd.read_excel(f.get_caminhoNotas(), f.get_sheetnameNotas())

browser.get('https://patospb.webiss.com.br/')

fazer_login(browser, cnpj, senha)

navegar_ate_nota(browser)

for indice in range(min(80, len(lerPlanilha))):  
    dados_cliente(browser, lerPlanilha, indice)
    descricao_servicos(browser)
    valor_servico(browser, indice)
    salvar_rascunho(browser)
    emitir(browser)