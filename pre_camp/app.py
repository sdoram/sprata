from flask import Flask, render_template, request, jsonify
import youtube

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/music", methods=["POST"])
def music_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    source_receive = request.form['source_give']
    crawling_receive = youtube.youtube.crawling(request.form['url_give'])
    crawling = []
    crawling.append(crawling_receive)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'source_code' : source_receive,
        'image':image,
        'star':star_receive,
        'comment':comment_receive,
        'artist':crawling[0][1],
        'title':crawling[0][0]
    }
    db.musics.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/music", methods=["GET"])
def music_get():
    music_list = list(db.musics.find({}, {'_id': False}))
    return jsonify({'musics':music_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

