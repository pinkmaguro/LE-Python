from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

"""
태그 중에서 특정 속성을 가지고 있는 태그를 선택하기 위해서 다음 메쏘드를 사용했다.
bsObj.findAll(tagName, tagAttributes :: dict)
"""

def get_select_class(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
        nameList = bsObj.findAll("span", {"class":"green"})
    except AttributeError as e:
        return None
    for name in nameList:
        print(name.get_text())


if __name__ == '__main__':
    url = 'http://www.pythonscraping.com/pages/warandpeace.html'
    get_select_class(url)