from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, random
from datetime import datetime


random.seed(datetime.now())

allIntLinks = set()
allExtLinks = set()

# 웹 페이지에서 찾은 내부 링크를 리스트로 뽑아낸다.
def getInternalLinks(bsObj, includeUrl):
    internalLink = []
    # a 태그를 모두 찾는다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLink:
                internalLink.append(link.attrs['href'])
                print(link.attrs['href'])
    print('Total size of interna links : ', len(internalLink))

# 웹 페이지에서 찾을 수 있는 모든 링크를 탐색한다.
pages = set()
def getLinks(homepage):
    global pages
    page = splitAddress(homepage)[0]
    html = urlopen(homepage)
    bsObj = BeautifulSoup(html, "html.parser")

    for link in bsObj.findAll('a', href=re.compile("^(https?).*" + page)):
        print(link)
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


# 아래의 코드는 재귀의 사용을 남발하고 있으므로 좋은 practice 가 아니다.
# 찾은 링크를 Queue 에 저장하는 것이 좋겠다.
def getWikiLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getWikiLinks(newPage)


# 웹 주소에 'http://'가 있으면 제거하고 '/' 를 기준으로 문자열을 나눈다.
# 원래의 코드 
# addressParts = address.replace('https://', '').replace('http://', '').split('/')
# http://www.daum.net -> www.daum.net
# 하지만 daum.net 부분만 추출하는 것이 맞음

def splitAddress(address):
    domain_pattern = re.compile('^(https?://)?(www)?(\w+\.)*(?P<url>\w+\.\w+)/?.*')
    domainParts = domain_pattern.match(address).group('url')
    return domainParts


def split_domain(address):
    """ 도메인 부분을 추출하기 위해서 내가 만든 함수
    """
    pattern = re.compile('^(https?://)?(\w+\.)*(?P<url>\w+\.\w+)/?.*$')
    domain = pattern.match(address).group('url')
    return domain            



homepage = "http://www.daum.net/"
startingPage = split_domain(homepage)
html = urlopen(homepage)
bsObj = BeautifulSoup(html, "lxml")
getInternalLinks(bsObj, "daum.net")