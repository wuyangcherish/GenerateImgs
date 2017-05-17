# -*- coding: utf-8 -*-
#
from flask import Flask, request, Response, send_file, jsonify

import requests
import codecs
import re
import jieba
import jieba.analyse
import sys

import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from PIL import Image
from wordcloud import WordCloud


reload(sys)
sys.setdefaultencoding('utf8')

from os import path

d = path.dirname(__file__)

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers',
                         'Origin, Authorization, Content-Type, Accept, Key')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, PUT, POST, DELETE')
    return response


@app.route("/search", methods=['GET'])
def search():
    url = 'http://baike.baidu.com/item/'
    value = request.args.get("person")
    searchUrl = url + value

    response = requests.get(searchUrl)

    # print response.content
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    # 获取简介
    brief = soup.find_all('dd', class_='basicInfo-item value')

    # 获取经历
    # detail = soup.find_all('div',class_="para",recursive=False)
    detail = soup.select('div[class="para"]')

    # 过滤字符

    def filterWord(word):
        new_text = word
        regx = ['(\^（.*?])', '(\(.*?\))']
        for reg in regx:
            new_text = re.sub(reg, '', new_text)
        return new_text

    str = ''
    for res in brief:
        str += res.text
    for ex in detail:
        str += filterWord(ex.get_text().strip('\n'))

    with codecs.open('info.txt', 'w', 'utf-8') as f:
        f.write(str)
    f.close()

    # ieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
    # sentence --> 待提取的文本
    # topK  TF/IDF 权重最大的关键词，默认 20
    # withWeight 为是否一并返回关键词权重值  默认为Flase
    # allowPOS 默认为空  不筛选

    # 读取文件
    text = open(path.join(d, 'info.txt')).read()

    # wordlist_after_jieba = jieba.analyse.extract_tags(text, topK=20,
    # withWeight=False, allowPOS=())     # 权重
    wordlist_after_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)

    # print wl_space_split
    info_mask = np.array(Image.open(path.abspath('../static/img/cat.png')))

    my_wordcloud = WordCloud(max_font_size=60, min_font_size=1,
                             mask=info_mask, background_color="white").generate(wl_space_split)

    my_wordcloud.to_file(path.abspath('../static/img/output.png'))

    return "Hello World"

if __name__ == "__main__":
    app.run(port=1024, debug=True)
