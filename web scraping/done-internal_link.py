from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, random
from datetime import datetime


def getInternalLinks(bsObj, includeUrl):
    internalLink = []
    count = 0
    # a 태그를 모두 찾는다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        count += 1
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLink:
                internalLink.append(link.attrs['href'])
                print(link.attrs['href'])
    print('Total size of interna links : ', len(internalLink))
    print('Total size of interna links : ', count)

if __name__ == '__main__':
    f = open('daum.html', 'r', encoding='utf-8')
    bsObj = BeautifulSoup(f, 'lxml')

    getInternalLinks(bsObj, 'daum.net')

    # tags = bsObj.findAll("a", href=re.compile("^(/|.*daum.net)"))
    # print(len(tags))

    # log = open('log.txt', 'wt')

    # for tag in tags:
    #     print(tag.attrs['href'])
    #     log.write(tag.attrs['href'] + '\n')

    # log.close()

