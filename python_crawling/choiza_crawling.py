import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbjjrm

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.mangoplate.com/search/%EC%88%98%EC%9A%94%EB%AF%B8%EC%8B%9D%ED%9A%8C?keyword=%EC%88%98%EC%9A%94%EB%AF%B8%EC%8B%9D%ED%9A%8C&page=10',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


lis=soup.select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li')

for li in lis:
    a_tag = li.select_one('figure > figcaption > div > a > h2')

    if a_tag is not None:
        image = li.select_one('figure > a > div > img')['data-original']
        url= li.select_one('figure > a')['href']
        title = a_tag.text
        grade = li.select_one('figure > figcaption > div > strong').text
        etc = li.select_one('figcaption > div > p.etc').text

        doc = {
            'image': image,
            'url': url,
            'title': title,
            'grade': grade,
            'etc': etc,
            'combo_num': 5
        }
        print(image, url, title, grade, etc, 5)
        db.lists.insert_one(doc)



