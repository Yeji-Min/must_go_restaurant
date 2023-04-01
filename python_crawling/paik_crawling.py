import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjjrm

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.mangoplate.com/search/%EB%B0%B1%EC%A2%85%EC%9B%90%EC%9D%98%203%EB%8C%80%EC%B2%9C%EC%99%95?keyword=%EB%B0%B1%EC%A2%85%EC%9B%90%EC%9D%98%203%EB%8C%80%EC%B2%9C%EC%99%95&page=10',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

lis=soup.select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li')


for li in lis:
    a_tag=li.select_one('figure > figcaption > div > a > h2')
    if a_tag is not None:
        title=a_tag.text
        grade=li.select_one('figure > figcaption > div > strong').text
        etc=li.select_one('figcaption > div > p.etc').text

        doc = {
            'title': title,
            'grade': grade,
            'etc': etc
        }
        print(title, grade, etc)
        db.paik.insert_one(doc)
