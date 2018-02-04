from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
import os

"""
어떤 웹페이지에의 src 속성이 그 웹페이지를 가르키면 
그 대상을 로컬 디스키에 같은 디렉토리 구조를 만들고 다운로드한다.
"""
downloadDirectory = "./download"
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    """ source 에 완전한 url 스트링을 가지고 있으면 source 를 url로 사용하고,
        그렇지 않으면 source를 baseUrl 의 하위 주소로 간주한다.
        이렇게 만든 url 주소에 baseUrl 스트링이 없다면 오류다.

    >>> getAbsoluteURL('http://xxx.com', 'www.xxx.com/abc')
    'http://xxx.com/abc'
    >>> getAbsoluteURL('http://xxx.com', 'abc')
    'http://xxx.com/abc'
    """
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://' + url
    else:
        url = baseUrl + '/' + source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    """
    baseUrl :  'http://xxx.com'
    absoluteUrl : 'http://xxx.com/js/abc.js'

    >>> getDownloadPath('http://xxx.com', 'http://xxx.com/js/abc.js', './download')
    './download/js/abc.js'
    """
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    directory = downloadDirectory + path.rsplit('/',1)[0]
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory + '/' + path.rsplit('/',1)[1]

html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html, 'lxml')
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    """
    "http://www.pythonscraping.com/misc/jquery.js?v=1.4.4"
    파일이름에서 위의 예처럼 ? 부분의 뒤는 제거해야한다.
    """
    webpath = download['src']
    match = re.match(r'[^?=]+' ,download['src'])
    if match:
        webpath_for_directory = match.group()
    else:
        continue

    fileUrl = getAbsoluteURL(baseUrl, webpath)
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, webpath_for_directory, downloadDirectory))

def _doctest():
    import doctest
    doctest.testmod(verbose = True)    
        
if __name__ == "__main__":
    _doctest()