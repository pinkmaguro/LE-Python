from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime

"""
위키피디아에 있는 링크 중에서 article 링크를 랜덤하게 하나 골라서 새로운 링크 탐색을 한다.abs
모든 링크를 탐색할려면 검색한 걸과를 큐/랜덤 큐/스택 에 저장한다.

같은 페이지를 다시 탐색하지 않으려면
탐색 기록을 set 으로 저장한다.
"""

def wiki_crawler():
    random.seed(datetime.datetime.now())
    def getLinks(articleUrl):
        html = urlopen('http://en.wikipedia.org'+articleUrl)
        bsObj = BeautifulSoup(html, 'html.parser')
        return bsObj.find('div',{'id':'bodyContent'}).findAll(
                    'a', href=re.compile("^(/wiki/)((?!:).)*$"))
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)

def wiki_crawler2():
    random.seed(datetime.datetime.now())
    pages = set()
    def getLinks(articleUrl):
        html = urlopen('http://en.wikipedia.org'+articleUrl)
        bsObj = BeautifulSoup(html, 'html.parser')
        for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)
    getLinks("")

if __name__ == '__main__':

    wiki_crawler2()