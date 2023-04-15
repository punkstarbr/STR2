import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp
import streamlink

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_livestream = "https://livestream.com/accounts/30360708"

# Abrir a página desejada
driver.get(url_livestream)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Get the page source again after scrolling to the bottom
html_content = driver.page_source

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    event_link = soup.find("a", class_="event_card_image ng-isolate-scope")
    event_url = "https://livestream.com" + event_link["href"]
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()

# Extract the stream URL using Streamlink
streams = streamlink.streams(event_url)
stream_url = streams["best"].url

# Write the stream URL in the TPAANGOLA.m3u8 file
try:
    with open('TPAANGOLA.m3u8', 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
        f.write(f"#EXTINF:-1,{event_url}\n")
        f.write(f"{stream_url}\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")

