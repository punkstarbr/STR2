import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp
import streamlink
import re


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

    # Find all the event links
    event_links = driver.find_elements(by='xpath', value="//a[contains(@class, 'event_card_image')]")

    # Loop through the event links and try to click on the first accessible one
    event_clicked = False
    for event_link in event_links:
        try:
            event_link.click()
            event_clicked = True
            break
        except:
            continue

    if not event_clicked:
        print("Error clicking on event link: No accessible events found.")
        driver.quit()
        return

    # Wait a few seconds for the event page to load
    time.sleep(5)

    # Get the page source again after scrolling to the bottom
    html_content = driver.page_source

    # Find the .m3u8 link in the performance log
    try:
        log_entries = driver.execute_script("return window.performance.getEntries();")
        link = ""
        for entry in log_entries:
            if ".m3u8" in entry['name']:
                link = entry['name']
                break
    except Exception as e:
        print(f"Error finding .m3u8 link: {e}")
        driver.quit()
        return

    # Write the .m3u8 link into the output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            f.write(f"{link}\n")
    except Exception as e:
        print(f"Error creating .m3u8 file: {e}")
        driver.quit()
        return

    # Close the driver
    driver.quit()


url1 = "https://livestream.com/accounts/31138991"
url2 = "https://livestream.com/accounts/3332377"

create_m3u8_file(url1, 'TPAANGOLA.m3u8')
create_m3u8_file(url2, 'TPAANGOLANEWS.m3u8')
