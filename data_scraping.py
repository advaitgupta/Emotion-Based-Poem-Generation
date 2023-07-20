import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
from langdetect import detect

chromedriver_path = '/opt/homebrew/Caskroom/chromedriver/104.0.5112.79/chromedriver'


base_url = "https://www.poetryfoundation.org/poems/browse#page={}&sort_by=recently_added"

chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(chromedriver_path)

with open('poems4.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Poem"])

    for page in tqdm(range(1, 2355)):

        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(base_url.format(page))

        time.sleep(5)

        page_source = driver.page_source

        driver.quit()

        # print(base_url.format(page))

        soup = BeautifulSoup(page_source, 'html.parser')

        # print(url)
        # print(response)

        poem_links = soup.find_all('h2', class_='c-hdgSans c-hdgSans_2')

        # print((poem_links))

        for link in poem_links:

            poem_url = link.find('a')['href']
            if poem_url.startswith("https://www.poetryfoundation.org/poems"):
                flag = True
            else:
                flag = False

            if flag is False:
                continue

            poem_response = requests.get(poem_url)
            poem_soup = BeautifulSoup(poem_response.content, 'html.parser')
            # print(poem_url)

            title = poem_soup.find('h1').text
            poem_text = poem_soup.find('div', class_='o-poem').text


            try:
                language = detect(poem_text)
            except:
                language = ""
            # print(language)
            if language == 'en':  # store only english poems
                writer.writerow([title, poem_text])

        time.sleep(0.5)
