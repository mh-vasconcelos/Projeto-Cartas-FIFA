# --- Arquivo que vai definir os critérios do driver do RPA e a função de RPA ---

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

os.environ['WDM_SSL_VERIFY'] = '0'
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("detach", True)
service = ChromeService("chromedriver.exe", options=options) 

driver = webdriver.Chrome(service=service, options=options)

# --- Função que chama o robô para procurar imagens dos artistas ---
def search_img(nome_artista):
    query = nome_artista.replace(" ", "+") + "+musician"
    driver.get(f"https://www.google.com/search?tbm=isch&q={query}")
    time.sleep(2) 

    try:
        # Seleciona a primeira imagem da grade
        primeira_img = driver.find_element(By.XPATH, '//img[@class="YQ4gaf"]')
        primeira_img.click()  # clique normal para abrir a visualização
        time.sleep(2)  # espera o carregamento da imagem maior

        # Pega o src da imagem maior
        url = driver.find_element(By.XPATH, '//img[@class="YQ4gaf"]').get_attribute("src")
        driver.quit()
        return url
    except:
        return None
    


    


