
import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
url_list = doc.select('ul.list_news2 a.link_txt')
for i, url in enumerate(url_list):
    print('ㅁㅁ NEWS -> {}번 ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ'.format(i+1))
    new_url = url['href']
    print('# URL: {}'.format(new_url))

    result = requests.get(new_url)

    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')

    contents.pop(-1)
    content = ''  # 본문 총합
    for info in contents:
        content += info.get_text()
    print('# 뉴스 제목: {}'.format(title))
    print('# 뉴스 본문: {}'.format(content))

