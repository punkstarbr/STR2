import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import yt_dlp


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

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll to the bottom of the page
scroll_y = 0
for _ in range(5):
    driver.execute_script(f"window.scrollTo(0, {scroll_y});")
    scroll_y += 1000
    time.sleep(2)


# Encontre todos os elementos 'a' na página
links = driver.find_elements(By.TAG_NAME, 'a')

# Obter todos os links presentes na página
all_links = [link.get_attribute('href') for link in links]

# Feche o driver
driver.quit()

# Crie um arquivo m3u com as informações dos links
with open("rtpplay", "w") as iptv_file:
    iptv_file.write("#EXTM3U\n")

    for link in all_links:
        try:
            ydl_opts = {
                'skip_download': True,
                'quiet': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                title = info.get("title", "unknown")
                thumbnail = info.get("thumbnail", "unknown")
                
                iptv_file.write(f'#EXTINF:-1 tvg-logo="{thumbnail}",{title}\n')
                iptv_file.write(f"{link}\n")

        except Exception as e:
            print(f"Erro ao extrair informações de {link}: {e}")
            continue

