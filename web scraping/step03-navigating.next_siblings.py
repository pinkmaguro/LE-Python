from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup



"""
.next_sibling(s)
.previous_sibling(s)

"""

def find_siblings(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        tagList = bsObj.find('table',{"id":"giftList"}).tr.next_siblings
    except AttributeError as e:
        return None
    for tag in tagList:
        print(tag)


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/page3.html"
    find_siblings(url)

    """
    테이블의 tr 은 하나의 row 에 대한 태그이다.
    find()로 찾은 첫 번쨰 tr 태그는 테이블은 항목이고 나머지 tr 태그는
    각각의 아이템 담고 있다.
    next_siblins 로 이 아이템들에 접근할 수 있다.
    """