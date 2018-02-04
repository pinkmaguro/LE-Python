from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, string

def cleanInput(input):
    input = re.sub('\n+', " ", input)      # muli line 제거
    input = re.sub('\[\d*\]', "", input)   # [12] 과 같은 주석 인덱스를 제거
    input = re.sub(' +', " ", input)       # 연속된 빈 칸 -> 한 개의 빈 칸
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    """ 입력 스트링을 길이가 n 인 조각으로 나눈다.
    """
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

def main():
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
    bsObj = BeautifulSoup(html, 'lxml')
    content = bsObj.find('div', {'id':'mw-content-text'}).get_text()
    ng = ngrams(content, 2)
    print(ng)
    print('2-grams count is: ' + str(len(ng)))
    

if __name__ == '__main__':
    main()