
# 컨테이너 td.overview-top
# 제목 : td.overview-top h4 a
# 감독 : td.overview-top div.txt-block span>a
# 배우 : td.overview-top div.txt-block span>a
# 장르 : td.overview-top p span

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text,'html.parser')


movies = html.select("td.overview-top")

for movie in movies:
    title = movie.select_one("h4 a").text.strip()
    info = movie.select("div.txt-block")
    director = info[0].select("span > a")
    actor = info[1].select("div.txt-block > a")
    
    genre_all = movie.select_one("p.cert-runtime-genre").text
    # director = movie.select("div:nth-of-type(3) span > a")
    # actor = movie.select("div:nth-of-type(4) > a")

    if "Action" not in genre_all:
        continue

    print("제목:", title)

    print("감독: ", end="")
    for d in director:
        print(d.text,end = " ")

    print("\n배우: ",end="")
    for a in actor:
        print(a.text,end= " ")

    print()
    print("="*50)