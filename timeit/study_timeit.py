"""
공식문서
https://docs.python.org/3/library/timeit.html

"""


import re, string, timeit

s = "string. With. Punctuation"
exclude = set(string.punctuation)
# table = maketrans(exclude, "")
regex = re.compile('[%s]' % re.escape(string.punctuation))

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

def test_re(s):  # From Vinko's solution, with fix.
    return regex.sub('', s)

def test_trans(s):
    return s.translate(table)

def test_repl(s):  # From S.Lott's solution
    for c in string.punctuation:
        s=s.replace(c,"")
    return s

repeat = 100000
print ("sets      :",timeit.Timer('f(s)', 'from __main__ import s,test_set as f').timeit(repeat))
print ("regex     :",timeit.Timer('f(s)', 'from __main__ import s,test_re as f').timeit(repeat))
# print ("translate :",timeit.Timer('f(s)', 'from __main__ import s,test_trans as f').timeit(repeat))
print ("replace   :",timeit.Timer('f(s)', 'from __main__ import s,test_repl as f').timeit(repeat))
