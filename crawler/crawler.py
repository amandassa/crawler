from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from bs4 import BeautifulSoup
seeds = []
with open('index.html') as fp:
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
  print(linha)

  #print("value: ", img.attrs.get("value")+'- '+ img.string +'\n')
'''
browser = webdriver.Chrome()
browser.get('http://www.agerba2.ba.gov.br/transporte/localidade_linha.asp')
element = browser.find_element(By.NAME, "sel_linha")
options = element.find_elements(By.TAG_NAME, "option")
for i in options:
  print('SELENIUM!!!! ----: ',i.string)
  break
'''
