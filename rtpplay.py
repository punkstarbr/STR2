import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp
from selenium.webdriver.common.by import By




# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_rtp = "https://www.rtp.pt/play/"

# Abrir a página desejada
driver.get(url_rtp)

# Aguardar alguns segundos para que a página seja carregada completamente
time.sleep(5)

# Encontrar o último vídeo na página e rolar até ele
for i in range(3):
    try:
        last_video = driver.find_element(By.XPATH, "//a[@class='ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link'][last()]")
        actions = ActionChains(driver)
        actions.move_to_element(last_video).perform()
        time.sleep(2)
    except:
        driver.execute_script("window.scrollBy(0, 10000)")
        time.sleep(2)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Encontre todos os elementos 'a' na página
links = driver.find_elements(By.TAG_NAME, 'a')

# Imprima todos os links presentes na página
for link in links:
    print(link.get_attribute('href'))

# Obter todos os links presentes na página
all_links = [link.get_attribute('href') for link in links]

# Fechar o driver
driver.quit()
