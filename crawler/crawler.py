from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import urllib.request
from bs4 import BeautifulSoup
seeds = []
with open('index.html', encoding='utf-8') as fp:
  soup = BeautifulSoup(fp, 'lxml')

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

browser = webdriver.Chrome()
browser.get('http://www.agerba2.ba.gov.br/transporte/localidade_linha.asp')
element = browser.find_element(By.NAME, "sel_linha")
option = element.find_element(By.TAG_NAME, "option")

#select = Select(driver.find_element_by_id('fruits01'))
#seleciona a linha pressiona tab e depois enter
option.select_by_value(seeds[0]._id).send_keys(Keys.TAB + Keys.RETURN)


browser.find_element_by_name('submit').click()
