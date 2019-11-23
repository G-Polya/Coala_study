import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                   headers={"User-Agent": "Mozilla/5.0"})

html = BeautifulSoup(raw.text,"html.parser")

# 컨테이너 ul.list_boxthumb li

movies = html.select("ul.list_boxthumb li")


# 제목 strong.tit_join

for movie in movies:
    title = movie.select_one("strong.tit_join a")
    url = title.attrs["href"]
    each_raw = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text,'html.parser')

    # 컨테이너 : div.detail_summarize
    # 평점 : em.emph_grade

    title = each_html.select_one("strong.tit_movie")
    score = each_html.select_one("em.emph_grade")

    print("제목:",title.text)
    print("평점:",score.text)


    # 장르 : info = dd.txt_main
    # info = movie.select_one("dd.txt_main")
    #
    # print(info)

    genre = movie.select("dd:nth-of-type(1)")
    print("장르:",genre.text)

    directors = movie.select("dd:nth-of-type(5) a")
    actors =movie.select("dd:nth-of-type(6) a")

    # 감독
    print("감독: ")
    for director in directors:
        print(director.text,end=" ")

    # 배우 :
    print("배우: ")
    for actor in actors:
        print(actor.text,end=" ")

    print(url)
    print("="*50)
