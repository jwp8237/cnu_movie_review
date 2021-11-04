# -> NAVER 영화(1개 선택) 리뷰 정보 수집(review, score, writer, date)

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206' \
      '657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionA' \
      'lready=false&isMileageSubscriptionReject=false&page=1'
doc = BeautifulSoup(requests.get(url).text, 'html.parser')

review_list = doc.select('div.score_result > ul > li')

for i, one in enumerate(review_list):
    print('## USER -> {}'.format(i+1))

#    review_text = one.select('div.score_reple > p > span',id='_filtered_ment_{}'.format(i))[0].get_text()
#    review_text = one.select('#_filtered_ment_{}'.format(i))[0].get_text().strip()

    score = one.select('div.star_score > em')[0].get_text()

    review = one.select('div.score_reple > p > span')[-1].get_text().strip()

    original_writer = one.select('div.score_reple dt em')[0].get_text().strip()

#   str, 'yyyy.mm.dd hh:mm'
    original_date = one.select('div.score_reple dt em')[1].get_text().strip()
    date = original_date[0:-6]

#   str, 'NAME(id)'
    idx_end = original_writer.find('(')
    writer = original_writer[0:idx_end]

    print('::REVIEW -> {}'.format(review))
    print('::WRITER -> {}'.format(writer))
    print(':: SCORE -> {}'.format(score))
    print(':: DATE -> {}'.format(date))
