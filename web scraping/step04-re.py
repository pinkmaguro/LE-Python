from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


"""
정규식을 속성 문자열 검색에 사용할 수 있다.

"""
def using_re(url):
    """  특정 디렉토리에 있는 img 로 시작하고 .jpg 로 끝나는 파일일을 검색한다.
         패턴 : "\.\.\/img\/gifts/img.*\.jpg"
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        pattern = r'\.\.\/img\/gifts/img.*\.jpg'
        tagList = bsObj.findAll('img',{"src":re.compile(pattern)})
    except AttributeError as e:
        return None
    for tag in tagList:
        print(tag)


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/page3.html"
    using_re(url)
