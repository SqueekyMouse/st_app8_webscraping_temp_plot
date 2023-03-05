import requests
from selectorlib import Extractor
from datetime import datetime
import time
# commit: scrap temp into csv n plot on webpage Sec38

URL='http://programmer100.pythonanywhere.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    response=requests.get(url,HEADERS)
    source=response.text
    return(source)

def extract(source):
    extractor=Extractor.from_yaml_file('extract.yaml')
    temp=extractor.extract(source)
    return(temp)

def store(temp):
    tnow=datetime.now()
    tstamp=tnow.strftime('%y-%m-%d-%H-%M-%S')
    with open('data.txt','a') as file:
        file.write(f'{tstamp},{temp}\n')

def data_file_init():
    with open('data.txt','r') as file:
        content=file.read()
    
    if not content.startswith('date,temperature'):
        with open('data.txt','w') as file:
            file.write('date,temperature\n')

if __name__=='__main__':
    data_file_init()
    while True:
        source=scrape(URL)
        temp=extract(source)['temp']
        store(temp)
        time.sleep(60)

