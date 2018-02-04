from random import randint

class Die:
    """ 주사위 하나를 나타내는 클래스 """
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)

    