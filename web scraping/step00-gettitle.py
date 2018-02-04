from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# html 정보를 가져오도록 urlopen() 메쏘드를 호출하면
# 페이지를 못찾는 경우와, 서버에 연결할 할 수 없는 경우에 대해서 예외 처리를 해줘야 한다.
# html 정보를 가져오더라도 원하는 내용(태그)이 없는 경우에도 대처해야 한다.

"""
bsObj.tag1.tag2  가 리턴하는 타입은
bs4.element.Tag 이다.
Tag 오브젝트의 __str__ 표현은 태그를 포함안 전체 스트링이다.
텍스트 내용만 가저올 때는 get_text() 메쏘드를 사용한다.
get_text() 를 사용하면 모든 태그 정보가 사라지므로 정보를 완전히 가공하기 전 까지는 
사용하지 않는 것이 좋다.

"""

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

if __name__ == '__main__':
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title == None:
        print('Title could not be found')
    else:
        print(type(title), title)
        print(title.get_text())
