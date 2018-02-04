import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def download_table():
    html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
    bsObj = BeautifulSoup(html, 'lxml')
    table = bsObj.findAll('table',{'class':'wikitable'})[0]
    rows = table.findAll('tr')

    with open('../tmp/editors.csv', 'wt', encoding='UTF8', newline='') as f:
        wt = csv.writer(f)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text())
            wt.writerow(csvRow)

if __name__ == '__main__':
    download_table()