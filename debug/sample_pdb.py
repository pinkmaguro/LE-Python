"""
공식문서 
https://docs.python.org/3/library/pdb.html

pdb.set_trace() 를 삽입하면 중단점 역할을 합니다.

몇 가지 디버거 명령어
h(elp)
w(here)
n(ext)
l(list)
c(ontinue)
q(quit)

대화 모드에서 자동으로 디버그 모드로 전환하는 예
pdb.run(main())
"""

import pdb

def add(a, b):
    # 이 위치에서 중단한다.
    pdb.set_trace()
    return a + b

def main():
    add(1, 2)

if __name__ == '__main__':
    main()