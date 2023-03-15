from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import urllib.request
from bs4 import BeautifulSoup
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
browser = webdriver.Chrome()
browser.get('http://www.agerba2.ba.gov.br/transporte/localidade_linha.asp')
#element = browser.find_element(By.NAME, "sel_linha")
options = browser.find_elements(by=By.TAG_NAME, value ="option")
print(options[0])
options[4].click()
botao = browser.find_elements(by=By.TAG_NAME, value ="input")
botao[1].click()
#select = Select(driver.find_element_by_id('fruits01'))
#seleciona a linha pressiona tab e depois enter
#options.select_by_value('005')

#browser.find_element_by_name('submit').click()
