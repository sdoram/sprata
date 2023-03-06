import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=Il-an3K9pjg&ab_channel=Anne-Marie'

url_receive = requests.get(url)

soup = BeautifulSoup(url_receive.text, 'html.parser')

# title = soup.select_one('div > a > ul > li:nth-child(1) > strong').get_text()
title = soup.select_one('#text > a').get_text()

print(title)
# print(soup)