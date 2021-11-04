import math
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206' \
      '657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionA' \
      'lready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

all_count = doc.select('strong.total > em')[0].get_text()

print(all_count)

total_page = math.ceil(int(all_count) / 10)
count = 0

for page in range(1, total_page + 1):
    new_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206' \
              '657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionA' \
              'lready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    doc = BeautifulSoup(requests.get(new_url).text, 'html.parser')

    review_list = doc.select('div.score_result > ul > li')

    for one in review_list:
        count += 1
        print('## USER -> {}'.format(count))
        print('## PAGE -> {}'.format(page))

        score = one.select('div.star_score > em')[0].get_text()

        review = one.select('div.score_reple > p > span')[
            -1].get_text().strip()

        original_writer = one.select('div.score_reple dt em')[
            0].get_text().strip()

        #   str, 'yyyy.mm.dd hh:mm'
        original_date = one.select('div.score_reple dt em')[
            1].get_text().strip()
        date = original_date[0:-6]

        #   str, 'NAME(id)'
        idx_end = original_writer.find('(')
        writer = original_writer[0:idx_end]

        print('::REVIEW -> {}'.format(review))
        print('::WRITER -> {}'.format(writer))
        print(':: SCORE -> {}'.format(score))
        print(':: DATE -> {}'.format(date))
