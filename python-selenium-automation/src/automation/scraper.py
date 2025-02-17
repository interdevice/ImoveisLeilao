import csv
import os
import time
import chardet
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from utils.chromedriver_manager import install_chromedriver

class Scraper:
    def __init__(self, download_path):
        self.download_path = download_path
        self.driver = None

        # Instalar ou atualizar o chromedriver
        install_chromedriver()

        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": self.download_path,
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True  # Permitir downloads automáticos
        })

        service = Service()  # O chromedriver_autoinstaller já define o caminho correto
        self.driver = webdriver.Chrome(service=service, options=options)

    def download_file(self):
        self.driver.get("https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp")
        time.sleep(5)  # Aguarda o carregamento da página

        self.driver.find_element(By.XPATH, '//select[@id="cmb_estado"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//select[@id="cmb_estado"]/option[@value="SP"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="btn_next1"]').click()
        time.sleep(2)

        # Usar pyautogui para interagir com a janela "Salvar como"
        pyautogui.write(os.path.join(self.download_path, 'Lista_imoveis_SP.csv'))
        pyautogui.press('enter')  # Pressionar Enter para salvar

        time.sleep(30)  # Aguarda o download completar

    def remove_lines_from_csv(self, file_path, lines_to_remove):
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())

        encoding = result['encoding']
        temp_file_path = file_path + '.tmp'
        with open(file_path, 'r', encoding=encoding) as infile, open(temp_file_path, 'w', encoding='utf-8', newline='') as outfile:
            reader = csv.reader(infile, delimiter=';')
            writer = csv.writer(outfile, delimiter=';')
            for line_num, row in enumerate(reader):
                if line_num not in lines_to_remove:
                    writer.writerow(row)
        os.replace(temp_file_path, file_path)

    def extract_data(self, file_path):
        self.remove_lines_from_csv(file_path, lines_to_remove=[0, 1])  # Remover as linhas 1 e 2 (índices 0 e 1)
        df = pd.read_csv(file_path, sep=';', header=0)  # Especificar que a primeira linha é o cabeçalho
        return df

    def open_links(self, links):
        for link in links:
            self.driver.get(link)
            time.sleep(5)
            
    def quit(self):
        if self.driver:
            self.driver.quit()