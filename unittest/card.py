import random
import unittest

Suits = 'C', 'D', 'H', 'S'

class Card:
    """implementing cards for black-jack game"""
    def __init__(self, rank, suit, hard=None, soft=None):
        self.rank = rank
        self.suit = suit
        self.hard = hard or int(rank)
        self.soft = soft or int(rank)

    def __str__(self):
        return "{0.rank!s}{0.suit!s}".format(self)



class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 1, 11)

class FaceCard(Card):
    """ cards for Jack, Queen, and King
    Facecard counts for 10 in black-jack
    """
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 10, 10)

def card(rank, suit):
    """ card factory """
    if rank == 1: return AceCard(rank, suit)
    elif 2<= rank < 11: return Card(rank, suit)
    elif 11<= rank < 14: return FaceCard(rank, suit)
    else: raise Exception("LogicError")

class Deck(list):
    """ Deck class
    초기화가 길지만 Deck 클래스가 직접적으로 Card 클래스 계층 구조나 특정 난수 생성기와 연관되지 않는다
    """
    def __init__(self, size=1, random=random.Random(),
                ace_class=AceCard, card_class=Card, face_class=FaceCard):
        super().__init__()
        self.rand = random
        for d in range(size):
            for s in Suits:
                cards = ([ace_class(1, s)] + [card_class(r, s) for r in range(2, 12)]
                      + [face_class(r,s) for r in range(12, 14)])
                super().extend(cards)
        self.rand.shuffle(self)                

"""
codes for UNITTEST 
"""
class TestCard(unittest.TestCase):
    def setUp(self):
        self.three_clbus = Card(3, 'C')
        
    def test_should_returnStr(self):
        self.assertEqual('3C', str(self.three_clbus))
        
    def test_should_getAttrValues(self):
        self.assertEqual(3, self.three_clbus.rank)
        self.assertEqual('C', self.three_clbus.suit)
        self.assertEqual(3, self.three_clbus.hard)
        self.assertEqual(3, self.three_clbus.soft)
        
        
class TestAceCard(unittest.TestCase):
    def setUp(self):
        self.ace_spades = AceCard(1, 'S')
        
    def test_should_returnStr(self):
        self.assertEqual('1S', str(self.ace_spades))
        
    def test_should_getAttrValues(self):
        self.assertEqual(1, self.ace_spades.rank)
        self.assertEqual('S', self.ace_spades.suit)
        self.assertEqual(1, self.ace_spades.hard)
        self.assertEqual(11, self.ace_spades.soft)

class TestCardFactory(unittest.TestCase):
    def test_rank1_should_createAceCard(self):
        c = card(1,'C')
        self.assertIsInstance(c, AceCard)
    def test_rank13_should_createFaceCard(self):
        c = card(13, 'C')
        self.assertIsInstance(c, Card)
    def test_otherRank_should_exception(self):
        with self.assertRaises(Exception):
            c = card(14,'D')


def suite2():
    s = unittest.TestSuite()
    load_from = unittest.defaultTestLoader.loadTestsFromTestCase
    s.addTests(load_from(TestCard))
    s.addTests(load_from(TestAceCard))
    return s

def suite3():
    s = unittest.TestSuite()
    load_from = unittest.defaultTestLoader.loadTestsFromTestCase
    s.addTests(load_from(TestCardFactory))
    return s

if __name__ == '__main__':
    allsuites = unittest.TestSuite([suite2(), suite3()])
    unittest.TextTestRunner(verbosity=2).run(allsuites)

