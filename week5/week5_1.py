# 네이버 영화 데이터 수집

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text,'html.parser')

# 컨테이너 dl.lst_dsc
# ul.lst_detail_t1 li는 왜 아닐까?  오히려 이쪽이 영화포스터도 포함하는데
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dl.lst_dsc
    title = m.select_one("dt.tit > a").text
    # 평점
    score = m.select_one("div.star_t1 a span.num").text
    # 배우 dl.1st_dsc dl.info_txt1 dd a

    # select 함수를 이용하는 방법
    # info = m.select("dl.info_txt1 dd")
    # # 장르 dl.1st_dsc dl.info_txt1 dd a
    # genre = info[0].select("a")
    # # 감독 dl.1st_dsc dl.info_txt1 dd a
    # director = info[1].select("a")
    # # 배우 dl.1st_dsc dl.info_txt1 dd a
    # actor = info[2].select("a")

    # 선택자를 사용하는 방법
    # 장르
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    # 감독
    director = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    # 배우
    actor = m.select("dl.info_txt1 dd:nth-of-type(1) a")

    print(title)
    print(score)
    for g in genre:
       print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("="*50)

    # 그리고 nth-of-type()의 앞에는 클래스 또는 아이디가 올 수 없기 때문에 해당하는 태그가 몇번째 태그인지도 꼭 확인해야합니다.
    # 무슨뜻?