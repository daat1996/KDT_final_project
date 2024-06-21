from flask import Blueprint, render_template, request 
from datetime import datetime
from transformers import BertTokenizer
from torch import optim
from transformers import BertForSequenceClassification
import pandas as pd
import random


deckDF = pd.read_csv('./data/character.csv',index_col=0)
deck = random.sample(deckDF.index.tolist(), 2)





## 인스턴스 생성
BP = Blueprint('main', __name__, template_folder='templates')


## BP 인스턴스 생성
data_BP=Blueprint('data', __name__, template_folder='templates', url_prefix="/")


@BP.route('/')
def index():
    return render_template('index.html')

@BP.route('/game')
def game_start():
    return render_template('game.html')

@BP.route('/help')
def open_help():
    return render_template('help.html')




@BP.route('/start')
def insight():
    deckDF = pd.read_csv('./data/character.csv',index_col=0)
    deck = random.sample(deckDF.index.tolist(), 2)
    my_card=f'../static/chrcard/{deck[0]}.jpg'
    your_card=f'../static/chrcard/{deck[1]}.jpg'
    my_force = deckDF.loc[deck[0]].force
    your_force = deckDF.loc[deck[1]].force

    cardList=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,'X']
    random.shuffle(cardList)
    image_paths = []
    for num in cardList:
        image_paths.append(f'../static/numcard/{num}.jpg')
    # 이미지 경로를 JavaScript 변수에 할당하기 위한 코드 생성
    js_code = f"var images = {image_paths};"

    # 생성된 JavaScript 코드를 HTML 파일에 저장
    with open("images.js", "w") as js_file:
        js_file.write(js_code)


    return render_template('start.html',my_card=my_card,
                           your_card=your_card, my_force=my_force, your_force=your_force)