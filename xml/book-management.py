from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import re

"""
빠르게 활용하는 파이썬 3.2 프로그래밍 XML 책 관리 프로그램
특징: XML 파싱은 DOM 오브젝트로 했지만 검색기능에서는 ElementTree 로 다시 파싱해서 기능을 수행함
개선한 내용: 책 제목 줄력하는 메쏘드를 알기 쉽게 간소화 했음, 메뉴를 출력하는 부분에서 메뉴 관련 내용을 리스트로 모아서
for문으로 한 번에 처리하게 했음
단축키와 인자를 받을 수 있게 _get_args 메쏘드를 추가 했음(정규식 사용)
다만, title 이외의 인자에서는 NoneType 에러가 발생함.  minidom 사용법을 더 공부해야함
앞으로: 시간이 난다면 클래스화 할 것
"""

### global
loopFlag = 1
xmlFD = -1        # xml 파일
BooksDoc = None   # Document 오브젝트,  xml.dom.minidom.parse 의 리턴값

### Menu
def printMenu():
    menu = [('Load xml','l'),
            ('Print dom to xml','p'),
            ('Quit program','q'),
            ('Print book list','b'),
            ('Add new book','a'),
            ('Search book title','s'),
            ('Make html','m')]
    # print('\nWelcom! Book Manager Program')
    # print('==========Menu==========')
    for menu, shortcut in menu:
        print(menu,':',shortcut)
    print('==========Menu==========')

def launcherFunction(menu):
    global BooksDoc
    if menu == 'l':
        BooksDoc = LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu.startswith('b'):
        PrintBookList('title')
    elif menu == 'a':
        ISBN = str(input('insert ISBN :'))
        title = str(input('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'e':
        keyword = str(input('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == 'm':
        keyword = str(input('input keyword code to the html :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print('-------------------')
        print(html)
        print('-------------------')
    else:
        print('error : unknown menu')

#### xml function implementation
def LoadXMLFromFile():
    """xml 파일 경로로부터 파일을 생성하고 파일로부터 document 오브젝트를 생성해서 리턴한다."""
    fileName = str(input ("please input file name to load :"))  # 읽어올 파일경로를 입력 받습니다.
    global xmlFD
 
    try:
        xmlFD = open(fileName)   # xml 문서를 open합니다.
    except IOError:
        print ("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)   # XML 문서를 파싱합니다.
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            return dom
    return None

def BooksFree():
    """ BooksDoc 에 document 오브젝트가 들어있으면 unlink 한다. """
    if checkDocument():
        BooksDoc.unlink()   # minidom 객체 해제합니다.
     
def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()

def PrintDOMtoXML():
    """ Return the XML that the DOM represents as a string.
        표현할 수 없는 텍스트에 대한 UnicodeError 를 피하기 위해서 'utf-8' 인코딩을 지정했다.
    """
    if checkDocument():
        print(BooksDoc.toxml('utf-8'))

def PrintBookList(tags):
    global BooksDoc
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None
        
    # booklist = BooksDoc.childNodes[0]
    # book = booklist.childNodes
    # for item in book:
    #     if item.nodeName == "book":  # 엘리먼트를 중 book인 것을 골라 냅니다.
    #         subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
    #         for atom in subitems:
    #             if atom.nodeName in tags:
    #                 print("title=",atom.firstChild.nodeValue)  # 책 목록을 출력 합니다.

    """ 위의 코드는 너무 장황하다. 메쏘드 인자로 tags 를 받지만 구현에서는 tags 는 title 로 고정되어 있다.
        아래는 간단한 버전으로 다시 코딩한 내용이다.
    """
    title_elements = BooksDoc.getElementsByTagName(tags)
    for elem in title_elements:
        print(tags, " : ", elem.firstChild.data)

def AddBook(bookdata):
    global BooksDoc
    if not checkDocument() :
        return None

    # Book 엘리먼트를 만듭니다.
    newBook = BooksDoc.createElement('book')
    newBook.setAttribute('ISBN', bookdata['ISBN'])
    # Title 엘리먼트를 만듭니다.
    titleEle = BooksDoc.createElement('title')
    # 텍스트 에릴먼트를 만듭니다.
    titleNode = BooksDoc.createTextNode(bookdata['title'])
    # 텍스트 노드와 Title 엘리먼트를 연결 시킵니다.
    try:
        titleEle.appendChild(titleNode)
    except Exception:
        print ("append child fail- please,check the parent element & node!!!")
        return None
    # else:
    #     titleEle.appendChild(titleNode)

    # Title를 book 엘리먼트와 연결 시킵니다.
    try:
        newBook.appendChild(titleEle)
        booklist = BooksDoc.firstChild
    except Exception:
        print ("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook)

def SearchBookTitle(keyword):
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None
        
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
        
    # Book 엘리먼트 리스트를 가져 옵니다.
    bookElements = tree.getiterator("book") 
    for item in bookElements:
        strTitle = item.find("title")
        if (strTitle.text.find(keyword) >=0 ):
            retlist.append((item.attrib["ISBN"], strTitle.text))
    
    return retlist    

def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    # DOM 개체를 생성합니다.
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)  # HTML 최상위 엘리먼트를 생성합니다.
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성
    body = newdoc.createElement('body')

    for bookitem in BookList:
        # Bold 엘리먼트를 생성합니다.
        b = newdoc.createElement('b')
        # 텍스트 노드를 만듭니다.
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)
    
        # <br> 부분을 생성합니다.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # title 부분을 생성합니다.
        p = newdoc.createElement('p')
        # 텍스트 노드를 만듭니다.
        titleText= newdoc.createTextNode("Title:" + bookitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # <br> 부분을 부모 에릴먼트에 추가합니다.
         
    # Body 엘리먼트를 최상위 엘리먼트에 추가시킵니다.
    top_element.appendChild(body)
    
    return newdoc.toxml()
    
def printBookList(blist):
    for res in blist:
        print (res)
    
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True

def _get_args(menu):
    pattern = re.compile(r'^\w\s(\w+)')
    arg = pattern.match(menu).groups()[0].lower()
    return arg

##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")