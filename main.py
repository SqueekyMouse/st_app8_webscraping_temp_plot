import requests
from selectorlib import Extractor
from datetime import datetime
import time
import sqlite3
# commit: scrap temp into sqlite db n plot on webpage Sec38

URL='http://programmer100.pythonanywhere.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

dbconnection=sqlite3.connect('data.sqlite')

def scrape(url):
    response=requests.get(url,HEADERS)
    source=response.text
    return(source)

def extract(source):
    extractor=Extractor.from_yaml_file('extract.yaml')
    temp=extractor.extract(source)
    return(temp)

def store(temp):
    tstamp=datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    cursor=dbconnection.cursor()
    cursor.execute("INSERT INTO temp VALUES(?,?)",(tstamp,temp))
    dbconnection.commit()

if __name__=='__main__':
    # data_file_init()
    while True:
        source=scrape(URL)
        temp=extract(source)['temp']
        store(temp)
        time.sleep(15)

