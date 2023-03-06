import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=zugAhfd2r0g&list=PLVI3CAcQB7GM7pBqn8WYVkSKn2QfUbS2E&index=14&ab_channel=JYPEntertainment'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#default-metadata-section')
    artist = soup.select_one('#info-rows')
    song = soup.select_one('#default-metadata')
    # print(song)
    print(artist)
    print(title)
    # print(soup)


    # class ="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/channel/UCs-QBT4qkj_YiQw1ZntDO3g" dir="auto" > LE SSERAFIM < / a >

else : 
    print(response.status_code)