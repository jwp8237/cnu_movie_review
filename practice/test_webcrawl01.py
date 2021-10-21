# 웹 크롤링 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup

# requests => 웹사이트 코드 복사 GET

# BeautifulSoup4 => requests GET 해온 코드에서 필요한 정보만 find 해서 찾아오기

url = 'https://news.v.daum.net/v/20211021152915953'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h3.tit_view')

print('# 뉴스 제목: {}'.format(title[0].get_text()))

