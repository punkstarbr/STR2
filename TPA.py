import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp
import streamlink


def create_m3u8_file(url_livestream, output_filename):
    # Configuring Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Instantiate the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Open the desired page
    driver.get(url_livestream)

    # Wait a few seconds for the entire content of the page to load
    time.sleep(5)

    # Get the page source again after scrolling to the bottom
    html_content = driver.page_source

    # Find the links and titles of the videos found
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        event_link = soup.find("a", class_="event_card_image ng-isolate-scope")
        event_url = "https://livestream.com" + event_link["href"]
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the driver
        driver.quit()

    # Extract the stream URL using Streamlink
    streams = streamlink.streams(event_url)
    stream_url = streams["best"].url

    # Write the stream URL in the output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            f.write("#EXT-X-VERSION:3\n")
            f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
            f.write("#EXTVLCOPT:http-user-agent=Firefox\n")
            f.write(f"{stream_url}\n")
    except Exception as e:
        print(f"Error creating .m3u8 file: {e}")


url1 = "https://livestream.com/accounts/30360708"
url2 = "https://livestream.com/accounts/31138991"

create_m3u8_file(url1, 'TPAANGOLA.m3u8')
create_m3u8_file(url2, 'TPAANGOLANEWS.m3u8')
