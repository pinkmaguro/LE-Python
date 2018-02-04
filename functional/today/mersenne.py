import collections

"""
간단한 strategy pattern
N제곱 연산을 수행하는 알고리즘(행동)을 주입받아서 클래스에서 사용함
"""

class Mersenel(collections.Callable):
    """ 메르센 수를 계산하는 클래스,
        Callable 을 상속해서 함수처럼 호출할 수 있게한다.
    """
    def __init__(self, algorithm):
        self.pow2 = algorithm
    def __call__(self, arg):
        return self.pow2(arg) - 1


def shifty(b):
    return 1 << b

def multy(b):
    if b == 0: return 1
    return 2 * multy(b - 1)

def faster(b):
    if b == 0: return 1
    if b % 2 == 1: return 2 * faster(b - 1)
    t = faster(b//2)
    return t * t

m1s = Mersenel(shifty)
m1m = Mersenel(multy)
m1f = Mersenel(faster)

if __name__ == '__main__':
    print(m1s(50))
    print(m1m(50))
    print(m1f(50))
    