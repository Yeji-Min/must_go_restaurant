from flask import Flask, render_template, jsonify, request
app: Flask = Flask(__name__)

import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjjrm


@app.route('/')
def home():
    return render_template('final_project.html')

## API 역할을 하는 부분
@app.route('/search', methods=['POST'])
def go():
    sample_receive = request.form['sample_give']
    return jsonify({'msg':'맛집노트를 구경해보세요:)'})


@app.route('/search', methods=['GET'])
def showRestaurants():
    restaurants = list(db.lists.find({}, {'_id': False}))
    return jsonify({'all_restaurants': restaurants})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
