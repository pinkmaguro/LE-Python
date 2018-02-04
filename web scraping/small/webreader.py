import requests
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_financial_statements(code):
    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
    html = requests.get(url).text



    # html = html.replace('<th class="bg r01c02 endLine line-bottom"colspan="8">연간</th>', "")
    html = html.replace("<span class='span-sub'>(IFRS연결)</span>", "")

    html = html.replace('\t', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')

    df_list = pd.read_html(html, index_col=0)
    df = df_list[0]


    print(df.columns)
    print(df.index)
    print(df)

if __name__ == "__main__":
    get_financial_statements('035720')
