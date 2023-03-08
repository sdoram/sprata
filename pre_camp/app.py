from flask import Flask, render_template, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
# from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
# import os
# import chromedriver_autoinstaller as AutoChrome
# import shutil
# import time
import youtube

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sdoram:RLATPAKS3@sparta.utt9hlo.mongodb.net/sparta?retryWrites=true&w=majority')
db = client.dbsparta1


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/music", methods=["POST"])
def music_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    source_receive = request.form['source_give']
    artist_receive = youtube.youtube.crawling(request.form['url_give'])
    artist = []
    artist.append(artist_receive)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'source_code' : source_receive,
        'title':title,
        'image':image,
        'star':star_receive,
        'comment':comment_receive,
        'artist':artist[0]
    }
    db.musics.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/music", methods=["GET"])
def music_get():
    music_list = list(db.musics.find({}, {'_id': False}))
    return jsonify({'musics':music_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

