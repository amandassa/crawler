from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import urllib.request
from bs4 import BeautifulSoup
import random
import time
from time import sleep
seeds = []
'''
with open('index.html', encoding='utf-8') as fp:
  soup = BeautifulSoup(fp)

#print("Título:", soup.title.string)
for opt in soup.find_all('option'):
  _id = 'id'
  nome = 'nome'
  linha = {
    _id: opt.attrs.get("value"),
    nome: opt.string
  }
  seeds.append(linha)
  # print(linha)

  #print("value: ", img.attrs.get("value")+'- '+ img.string +'\n')

'''
def sleep():
  time.sleep(random.uniform(0.1, 2))

linhas = []
browser = webdriver.Chrome()
browser.get('http://www.agerba2.ba.gov.br/transporte/localidade_linha.asp')
#element = browser.find_element(By.NAME, "sel_linha")
options = browser.find_elements(by=By.TAG_NAME, value ="option")
for i in range(0,5):
    parada = dict(id = '', nome = '')
    horario = dict(dia = '', horarios = [])
    linha = dict(codigo = '', nome = '', paradas = [], horariosDestino = [], horariosOrigem = [], )    
    options[i].click()
    sleep()
    linha["codigo"] = options[i].get_attribute("value")
    linha['nome'] = options[i].text
    botoes = browser.find_elements(by=By.TAG_NAME, value ="input")
    for btn in botoes:
        if btn.get_attribute("value") == "Consultar":
            btn.click()
            sleep()

    tds = browser.find_elements(by=By.TAG_NAME, value ="td")
    for j in tds:
        #if j.get_attribute("width") == '15%':                       
         #   parada['id'] = j.find_element(by=By.TAG_NAME, value ="font").text
        if j.get_attribute("width") == '78%':
            #print(j.find_element(by=By.TAG_NAME, value ="font").text)
            #parada['nome'] = j.find_element(by=By.TAG_NAME, value ="font").text
            linha['paradas'].append(j.find_element(by=By.TAG_NAME, value ="font").text)
    
    links = browser.find_elements(by=By.TAG_NAME, value="a")
    for l in links:
        if l.find_element(by=By.TAG_NAME, value="font").text == 'Horários e Frequência':
            l.click()
            break
    

      
       
        
        #print(linha['paradas'])
        #parada['id'] = ''
        #parada['nome'] = ''

    print(linha['codigo']+'\n')
    print(linha['nome']+'\n')
    for k in linha['paradas']:
        print(k+'\n')
    break
#font = tds[1].find_element(by=By.TAG_NAME, value ="font")
#print(font.text)


#select = Select(driver.find_element_by_id('fruits01'))
#seleciona a linha pressiona tab e depois enter
#options.select_by_value('005')

#browser.find_element_by_name('submit').click()
