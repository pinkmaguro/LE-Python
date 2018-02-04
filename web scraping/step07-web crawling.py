from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, random
from datetime import datetime

pages = set()
random.seed(datetime.now())

# 웹 페이지에서 찾은 내부 링크를 리스트로 뽑아낸다.
def getInternalLinks(bsObj, includeUrl):
    internalLinks = set()
    # a 태그를 모두 찾는다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.add(link.attrs['href'])
    return list(internalLinks)

# 웹 페이지에서 찾은 외부 링크를 리스트로 뽑아낸다.
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = set()
    # 'http' 나 'www' 로 시작하는 링크를 수집한다.
    for link in bsObj.findAll('a',
            href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.add(link.attrs['href'])
    return list(externalLinks)

# 웹 주소에 'http://'가 있으면 제거하고 '/' 를 기준으로 문자열을 나눈다.
def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts

# 만약 외부 링크를 발견하지 못하면 내부링크 중에서 외부 링크를 찾아서 리턴한다.
# 책의 코딩에 오류가 있으서 수정했다.
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        print('Search from internal links')
        internalLinks = getInternalLinks(bsObj, startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0, 
                                  len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
    
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)
            
followExternalOnly("http://oreilly.com")