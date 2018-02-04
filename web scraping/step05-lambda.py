from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


"""
속성에 접근하는법
myImgTag.attrs['src']

람다식 표현
soup.findAll(lambda tag: len(tag.attr) ==2)
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
"""
