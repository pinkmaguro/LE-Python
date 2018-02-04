"""
pandas 에서 html table 을 읽게해주는 모듈 html5lib 인스톨
conda install html5lib

"""

import pandas as pd
from bs4 import BeautifulSoup

# html 안의 첫 번쨰 테이블 정보를 불러온다.  편하다.
df = pd.read_html('./table.html', encoding='utf-8')[0]

print(df.iloc[1])