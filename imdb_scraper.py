import requests
import datetime
from bs4 import BeautifulSoup
from tqdm import tqdm
from ascii import genres


current_year = int(datetime.datetime.now().year)
input_year = int(input("Inserir ano inicial (eg. 2009): "))
print(genres)
input_genres = input("Insere os generos, separados por virgulas: ").lower().replace(" ", "")
if input_year > current_year:
    print(f"Ano inicial não pode ser depois de {current_year}")
else:
    for year in tqdm(range(input_year, current_year+1), desc="Request progress", position=0):
        url = "https://www.imdb.com/search/title/?release_date=" + str(year) + "," + str(year) + "&genres=" + input_genres
        response = requests.get(url, timeout=15)
        movie_soup = BeautifulSoup(response.content, "html.parser")
        movieList = movie_soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
        i = 1
        for div_item in tqdm(movieList):
            div = div_item.find('div', attrs={'class': 'lister-item-content'})
            print (str(i) + '.',)
            header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
            print ('Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
            i += 1