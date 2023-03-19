from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from time import sleep

import json

seeds = []

def sleep():
  time.sleep(random.uniform(0.1, 2))

arquivo = open("linhas.json", 'w')

linhas = []
browser = webdriver.Chrome()
browser.get('http://www.agerba2.ba.gov.br/transporte/localidade_linha.asp')
options = browser.find_elements(by=By.TAG_NAME, value ="option")
for i in range(0,5):
    parada = dict(id = '', nome = '')
    horario = dict(dia = '', horarios = [])
    linha = dict(codigo = '', nome = '', paradas = [], horariosDestino = [], horariosOrigem = [])    
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
        if j.get_attribute("width") == '78%' and (j.find_element(By.TAG_NAME, value="font").text != "LOCALIDADES"):
            linha['paradas'].append(j.find_element(by=By.TAG_NAME, value ="font").text)
    
    links = browser.find_elements(by=By.TAG_NAME, value="a")
    for l in links:
        if l.find_element(by=By.TAG_NAME, value="font").text == 'Horários e Frequência':
            l.click()
            sleep()
            break
    
    tdscinza = browser.find_elements(By.CSS_SELECTOR, 'td.cinza02')
    tdsdias = []
    for td in tdscinza:
      if len(td.text) == 3: 
        tdsdias.append(td)

    tdshorarios = []
    for td in browser.find_elements(by=By.TAG_NAME, value ="td"):
        if td.get_attribute("width") == "7%":
            tdshorarios.append(td)
    
    for dia in tdsdias:
        tdshorarios.remove(dia)

    c=0
    for horario in tdshorarios:
        if c < 7:
          linha["horariosOrigem"].append(horario.text)
          c += 1
        else:
            linha["horariosDestino"].append(horario.text)

    ######## LISTA DE HORARIOS: [seg,ter,qua,qui,sex,sab,dom]

    print(linha['codigo']+'\n')
    print(linha['nome']+'\n')
    for k in linha['paradas']:
        print(k+'\n')
        
    linhas.append(linha)

    voltar1 = browser.find_elements(by=By.TAG_NAME, value ="a")
    for n in voltar1:
        if n.text == 'Voltar':
            n.click()
            break
    sleep()
    voltar2 = browser.find_elements(by=By.TAG_NAME, value ="a")
    for s in voltar2:
        if s.text == 'Voltar':
            s.click()
            break

jstring = json.dumps(linhas,ensure_ascii=False).encode()
arquivo.write(str(jstring.decode()))
