import requests 
import datetime 
from bs4 import BeautifulSoup as BS 


def zapros():
    url = "http://www.ztec.com.ua/ztec/schedule/schedule/view"
    r = requests.get(url)

    if r.status_code == 200:

        soup = BS(r.text, 'html.parser')  

        parsData=soup.find('h2')
        print(parsData)

        parsPar=soup.find_all('table', class_='table table-striped')
        print(parsPar)
    
zapros