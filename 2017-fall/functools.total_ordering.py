import functools
import unittest
import doctest

@functools.total_ordering
class Card:
    """
    >>> 1+2+3
    6
    >>> c1, c2 = Card(3,'S'), Card(4,'D')
    >>> c1 != c2
    True
    >>> c1 < c2
    True
    """
    # 인스턴스의 어떤 변수를 사용할지 명시해둠,  fast access, save memory
    __slots__ = {'rank', 'suit'} 

    # 클래스가 호출되었을 때 실행됨. 팩토리와 같은 역할
    def __new__(cls, rank, suit):
        self = super().__new__(cls)
        self.rank = rank
        self.suit = suit
        return self

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank


class TestCardTotalOrder(unittest.TestCase):
    def setUp(self):
        self.c1 = Card(3, 'C')
        self.c2 = Card(4, 'D')
    
    def tearDown(self):
        del self.c1
        del self.c2

    def test_equality(self):
        self.assertFalse(self.c1 == self.c2)

    def test_order(self):
        self.assertTrue(self.c1 < self.c2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    load_from = unittest.defaultTestLoader.loadTestsFromTestCase
    suite.addTests(load_from(TestCardTotalOrder))
    unittest.TextTestRunner(verbosity=2).run(suite)
    doctest.testmod()