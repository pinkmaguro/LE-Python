from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re



"""
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- 태그 이름을 사용한 검색은 처음 하나의 결과만 리턴한다.
soup.a
- 태그의 children 은 .contents 로 얻을 수 있다.
soup.head.contents, ...contents[1]
- children 요소를 리스트 대신 iterator 로 얻을려면  .children 을 사용한다.
link_tag.children
- 하위 자손을 모두 검색할려면 .descendents 를 사용한다.
태그, 텍스트 모두 포함해서 검색함

findAll 의 검색을 children 으로 한정하려면 .children 을 findAll 뒤에 붙여준다.

"""

def findAll_children(file):
    try:
        f = open(file, 'r', encoding='UTF8')
    except IOError as e:
        return None
    try:
        html = f.read()
        bsObj = BeautifulSoup(html, 'lxml')
        tagList = bsObj.find("li", {'class':'dropdown'})

    except AttributeError as e:
        return None
    
    for i,tag in enumerate(tagList):
        print(i, tag)
    print('result length : ', len(tagList))

def navigating_tree(text):
    """ BeatifulSoup 의 표현에 대한 테스트를 쉽게 하고 그 결과를 알아보기 쉽게하기 위해서
        테스트 내용을 리스트로 저장했다.
    """
    soup = BeautifulSoup(text, 'html.parser')
    test_list = [('soup.head', soup.head),
                 ('soup.body.b', soup.body.b),
                 ('soup.a', soup.a),
                 ('soup.find_all("a")', soup.find_all("a")),
                 ('soup.p.contents', soup.p.contents),
                 ('soup.body.contents[2]', soup.body.contents)]
    
    def _test(test_list, *test_index):
        for index in test_index:
            print(test_list[index][0])
            print(test_list[index][1], '\n')

    _test(test_list, -2)

def descendent(text):
    soup = BeautifulSoup(text, 'html.parser')
    print('All descendents')
    for i, child in enumerate(soup.descendants):
        print(i, child)


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/page3.html"
    file = 'structure.html'
    html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<div class="link">
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
</div>

<p class="story">...</p>
"""
    # findAll_children(file)
    navigating_tree(html_doc)
    # descendent(html_doc)
    """

    """
