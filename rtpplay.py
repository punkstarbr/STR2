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
url_rtp = "https://search.bilibili.com/all?keyword=blink+182&from_source=webtop_search&spm_id_from=333.1007&search_source=5&duration=3"

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

# Crie um arquivo m3u com as informações dos links
with open("rtpplay.m3u", "w") as iptv_file:
    iptv_file.write("#EXTM3U\n")

    for link in all_links:
        try:
            ydl_opts = {
                'skip_download': True,
                'quiet': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                url = info.get("url", "unknown")
                title = info.get("title", "unknown")
                thumbnail = info.get("thumbnail", "unknown")
                
                iptv_file.write(f'#EXTINF:-1 group-title=\"RTPPLAY\" tvg-logo="{thumbnail}",{title}\n')
                iptv_file.write(f"{url}\n")

        except Exception as e:
            print(f"Erro ao extrair informações de {link}: {e}")
            continue
