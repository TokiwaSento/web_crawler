import requests
from bs4 import BeautifulSoup
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; X64"}
for i in range(10):
    rank = i*25
    url = "https://movie.douban.com/top250?start=" + str(rank) + "&filter="
    response = requests.get(url, headers=head)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    all_movies = soup.findAll("div", attrs={"class": "info"})
    for movie in all_movies:
        all_links = movie.findAll("a")
        for link in all_links:
            name = link.find("span")
            print(name)
        point = movie.findAll("span", attrs={"class": "rating_num"})
        for the_point in point:
            print(the_point)