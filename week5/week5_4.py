import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent':'Mozilla/5.0'})

html = BeautifulSoup(raw.text,'html.parser')

# 컨테이너 dl.lst_dsc
# ul.lst_detail_t1 li는 왜 아닐까?  오히려 이쪽이 영화포스터도 포함하는데
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dl.lst_dsc
    title = m.select_one("dt.tit > a")
    url = title.attrs["href"]
    print("="*50)
    print(title.text)

    each_raw = requests.get("https://movie.naver.com"+url,headers={'User-Agent':'Mozilla/5.0'})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 컨테이너 div.score_result>ul>li
    # 평점 div.star_score em
    # 리뷰 div.score_reple p
    reviews = each_html.select("div.score_result>ul>li")
    for r in reviews:
        stars = r.select_one("div.star_score em").text
        reple = r.select_one("div.score_reple p").text.strip()

        print(stars, reple)
    # https://movie.naver.com/movie/bi/mi/basic.nhn?code=167605
    # /movie/bi/mi/basic.nhn?code=167605