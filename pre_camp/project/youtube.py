from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller as AutoChrome
import shutil

def chromedriver_update(): # 크롬드라이버 자동 업데이트
    chrome_ver = AutoChrome.get_chrome_version().split('.')[0] # 현재 크롬 버전 확인
    current_list = os.listdir(os.getcwd()) # 현재 디렉토리 파일,폴더 리스트 
    chrome_list = []
    for i in current_list:
        path = os.path.join(os.getcwd(),i) # 현재 디렉토리에 파일,폴더를 더해 주소를 만듦
        if os.path.isdir(path): # 폴더만 추린다.
            if 'chromedriver.exe' in os.listdir(path): #'chromedriver.exe'가 해당 폴더에 있는지 확인
                chrome_list.append(i)
                
    old_version = list(set(chrome_list) - set([chrome_ver])) # 크롬드라이버가 있는 폴더중에 최신폴더 제외
    
    for i in old_version:
        path = os.path.join(os.getcwd(),i) # 구버전 폴더 경로
        shutil.rmtree(path)                    # 구버전 폴더 삭제
    
    if not chrome_ver in current_list:     # not 최신버전 in 현재 경로:
        AutoChrome.install(True)           # 크롬 드라이버 설치
    else: pass                             # pass
        
     
youtube_link = 'https://www.youtube.com/watch?v=jKbWN9qgeiY&ab_channel=1theK%28%EC%9B%90%EB%8D%94%EC%BC%80%EC%9D%B4%29' 
chromedriver_update()

def link (youtube_link):
    if youtube_link.find("youtu.be") == -1:
            url = youtube_link.split("watch?v=")[1][0:11]
            print(url)
    elif youtube_link.find("youtube.com") == -1:
            url = youtube_link.split(".be/")[1]
            print(url)
link(youtube_link)



class youtube:     
    def crawling (link): # youtube 크롤링 
        chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
        path = os.path.join(os.getcwd(),chrome_ver)
        path = os.path.join(path,'chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument("headless") # 백그라운드 실행
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.get(url=link)
        driver.implicitly_wait(100) # 최대 100초 대기, 결과 찾으면 종료
        
        music_crawling = driver.find_elements(By.ID, 'default-metadata')[0] # 제목
        artist_crawling = driver.find_elements(By.ID, 'default-metadata')[1] # 가수
        album_crawling = driver.find_elements(By.ID, 'default-metadata')[2] # 앨범
        
        music = music_crawling.get_attribute('innerText')
        artist = artist_crawling.get_attribute('innerText')
        album = album_crawling.get_attribute('innerText')

        print(music)
        print(artist)
        print(album)
        return music,artist,album,driver.close()

    # while(True): # 브라우저 닫힘 방지
    #     pass
    


if __name__ == "__main__":
    chromedriver_update() # 크롬드라이버 자동 업데이트
    youtube.crawling(youtube_link)
