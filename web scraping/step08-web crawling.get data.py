from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

"""
웹 크롤링은 데이터를 얻기위해서 하는 것이다.
타겟 데이터의 우치와 얻어오는 방법을 연구해서 크롤러 안에 넣어야 한다.
아래에서는 특정 태그나 id 정보로 html 내의 정보를 출력하고 있다.
"""
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id ="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("") 

