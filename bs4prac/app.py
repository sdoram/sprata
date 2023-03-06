import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import chromedriver_autoinstaller as AutoChrome
import shutil

# def chromedriver_update(): # 크롬드라이버 자동 업데이트
#     chrome_ver = AutoChrome.get_chrome_version().split('.')[0] # 현재 크롬 버전 확인
    

#     current_list = os.listdir(os.getcwd()) # 현재 디렉토리 파일,폴더 리스트 
#     chrome_list = []

#     for i in current_list:
#         path = os.path.join(os.getcwd(),i) # 현재 디렉토리에 파일,폴더를 더해 주소를 만듦
#         if os.path.isdir(path): # 폴더만 추린다.
#             # print(f'폴더명 : {i} / 내용물 {os.listdir(path)}') # 그 폴더의 내용물을 리스트로 출력한다.
#             if 'chromedriver.exe' in os.listdir(path): #'chromedriver.exe'가 해당 폴더에 있는지 확인
#                 chrome_list.append(i)
                
#     old_version = list(set(chrome_list) - set([chrome_ver])) # 크롬드라이버가 있는 폴더중에 최신폴더 제외
    
#     for i in old_version:
#         path = os.path.join(os.getcwd(),i) # 구버전 폴더 경로
#         shutil.rmtree(path)                    # 구버전 폴더 삭제
    
#     if not chrome_ver in current_list:     # not 최신버전 in 현재 경로:
#         AutoChrome.install(True)           # 크롬 드라이버 설치
#     else: pass                             # pass
    
       
# def selenium_test():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome("./chromedriver.exe", options=options)
    # chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
    # path = os.path.join(os.getcwd(),chrome_ver)
    # path = os.path.join(path,'chromedriver.exe')
    # print(path)
    # URL = 'https://www.google.co.kr/'
    # driver = webdriver.Chrome(str(path))
    # driver.get(url=URL)
    
    # while(True):
    #     pass