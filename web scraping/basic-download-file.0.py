from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

fileLocation = "http://pythonscraping.com/misc/jquery.js?v=1.4.4"
urlretrieve(fileLocation, r'.\downloaded\some.js')
