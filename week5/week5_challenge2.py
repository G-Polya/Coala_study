import requests
from bs4 import BeautifulSoup
from urllib.request import  urlretrieve


raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers={"User-Agent": "Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')

movies = html.select("td.overview-top")

for movie in movies:
    title = movie.select_one("h4 a")
    url = title.attrs["href"]
    each_raw = requests.get("https://www.imdb.com/"+url,headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    poster = each_html.select_one("div.poster img")

    # print(poster)
    poster_src = poster.attrs["src"]

    print(title.text)
    print("https://www.imdb.com/" + url)
    print("=" * 50)

    urlretrieve(poster_src, "challege2_poster/" + title.text[:2] + ".png")
    # div.slate_wrapper div.poster img


