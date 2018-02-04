from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup



"""
Tag 오브젝트를 검색할 때는 findAll 또는 find 메쏘드를 사용한다.

findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text , keywords)

# tag 인자
.findAll({'h1','h2','h3'}) // 태그를 파이썬 리스트로 넘겨줄 수도 있다.

# attributes 인자
.findAll("span", {"class":"green", "class":"red"}) // 딕셔너리로 속성 정보를 넘겨준다.

# recursive 인자::boolean
탐색 깊이 레벨을 정한다.

# text 인자
특정 문자열을 포함하는 태그를 검색
nameList = bsObj.findAll(text="the prince")
print(len(nameList))

# limit 인자
검색 결과의 갯수,  limit=1 이면 find 메쏘드와 동일하다.

# keywords 인자
특정 속성을 포함하는 태그를 검색
allText = bsObj.findAll(id="text")

keywords 인자는 안 쓰는 것이 좋음.
keywords 표현은 RE 나 lambda 표현으로 대신할 수 있음
bsObj.findAll(id="text")
bsObj.findAll("", {"id":"text"})
키워드에서 class 를 표시할 때는 class_ 를 사용함 (class 의 파이썬의 예약어라서 그대로 사용할 수 없음)

"""

def findAll_tag(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        tagList = bsObj.findAll(['h1','h2'])  
    except AttributeError as e:
        return None
    for tag in tagList:
        print(tag)

if __name__ == '__main__':
    url = 'http://www.pythonscraping.com/pages/warandpeace.html'
    findAll_tag(url)

    """
    <h1>War and Peace</h1>
    <h2>Chapter 1</h2>
    """
