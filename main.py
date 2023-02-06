from selenium.webdriver import Keys
from seleniumwire import webdriver
import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
import pandas as pd
import openpyxl
from time import sleep
import requests
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class BotChrome:

    def __init__(self):
#         ua = UserAgent()
#         self.chrome_options = uc.ChromeOptions()
#         #self.chrome_options.add_argument('--headless')
#         self.chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# +"AppleWebKit/539.36 (KHTML, like Gecko)"
# +"Chrome/87.0.4280.141 Safari/537.36")
#         self.chrome_options.add_argument(r'--user-data-dir=C:\DadosNavegador')
        
#         self.driver = uc.webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
#         self.wait = WebDriverWait(self.driver, 120)


        self.options = uc.ChromeOptions()
        self.options.add_argument('--proxy-server=138.185.46.22:3128')
        self.driver = uc.Chrome(options = self.options)

        #self.url = 'https://www8.receita.fazenda.gov.br/simplesnacional/aplicacoes.aspx?id=21'
        

    def get_element_by_xpath(self, xpath, ec=None):
        ec = ec if ec else EC.presence_of_element_located
        return self.wait.until(ec((By.XPATH, xpath)))

    def acessar(self):
        self.driver.get('https://www.google.com.br')
        sleep(40)
    
    def pega_dados(self):
        cnpj_list = [i.text for i in self.driver.find_elements(By.XPATH,'//td[3]')]
        book = openpyxl.load_workbook('cnpjs_br.xlsx')
        tabela = book.active
        for i in cnpj_list:
            tabela.append([i])
        tabela.column_dimensions['A'].width = 80
        book.save('cnpjs_br.xlsx')
    
    def ler_excel(self):
        df = pd.read_excel('cnpjs_br.xlsx')
        data = df.to_dict(orient='records')
        novo = data
        for i in novo:
            yield i['CNPJ']
        
    def qqcoisa(self):
        #self.driver.switch_to.frame('frame')
        
        for i in self.ler_excel():
           
            sleep(40000)
            #self.driver.find_element(By.XPATH,"//input[@id='Cnpj']").send_keys(f'{i}',Keys.ENTER)
           
            sleep(40)
        
        
        #self.driver.find_element(By.XPATH,'//input[@id="Cnpj"]').click()
        

if __name__=='__main__':
    bot = BotChrome()
    bot.acessar()
    bot.qqcoisa()
    #bot.pega_dados()
    
##############################################################################################

# from playwright.sync_api import sync_playwright
# from time import sleep
# from fake_useragent import UserAgent

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     ua = UserAgent()
#     page = browser.new_page(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')

#     page.goto("http://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes.aspx?id=21")
#     page.pause()
#     print(page.title())
#     browser.close()