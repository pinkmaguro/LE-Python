from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


"""
위키피디아의 링크 정보 중에서 article link 와 그외의 링크를
구분하는 로직이 필요하다.

article link 는 다음 특징을 가진다.
- <div id="bodyContent"> 안에 들어있다.
- URL 에 세미콜론을 포함하지 않는다.
- URL 이 /wiki/ 로 시작한다.
"""
def web_crawler(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                print(link.attrs['href'])
    except AttributeError as e:
        return None

def web_crawler_with_constrains(url):
    """ 정규식을 사용해서 링크 스트링에 제한을 두었다.
        /wiki/ 로 시작하는 스트링 중에 : 를 포함하지 않는 스트링을 검색한다.
        
        expected resutls :
        /wiki/Peter_Riegert
        /wiki/Jacob_Vargas
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        for link in bsObj.find("div", {"id":"bodyContent"}).findAll(
            "a", href=re.compile("^(/wiki/)((?!:).)*$")):
            if 'href' in link.attrs:
                print(link.attrs['href'])
    except AttributeError as e:
        return None

if __name__ == '__main__':
    url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
    # web_crawler(url)
    web_crawler_with_constrains(url)