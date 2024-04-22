import requests
from bs4 import BeautifulSoup

def read_html():
    URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    response = requests.get(url=URL)
    return response.text

def generate_movies_list(html):
    soup = BeautifulSoup(html,'html.parser')
    movies_tags = soup.find_all(name='h3',class_="title")
    movies_list = [tag.getText() for tag in movies_tags]
    return movies_list

def create_movies_file(movies_list):
    with open('./hundred_movies_to_watch.txt','w',encoding='utf-8') as file:
        for i in range(len(movies_list)-1,-1,-1):
            file.write(f"{movies_list[i]}\n")

html = read_html()
movies_list = generate_movies_list(html)
create_movies_file(movies_list)




