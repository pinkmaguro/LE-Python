"""
pingpong(x) = ?
x 가 7의 배수나 7을 포함하는 숫자면 증가의 방향을 바꾼다.
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 6 5 4

7, 14, 17, 21, 27, ... 에서 증가의 방향이 1에서  -1로 또는 -1에서 1로 바뀐다.

변수를 사용할 수 있으면 그리 어렵지 않게 풀 수 있지만
변수의 사용, 루프를 상요하지 않는다는 제약을 두면 어려워진다.

스퀀스의 이전 결과를 사용해서 다음 원소를 계산하는 문제이기 떄문에
functools 의 reduce 함수를 사용하면 편하게 풀 수 있다.

모듈 임포트 없이 풀어볼려고 고뇌했다.
기본적인 테스트를 위한 코드를 넣었다.
사용한 함수의 갯수가 많기 때문에
처음 읽는 사람도 알기 쉽게 하기 위해서 
기능을 설명하는 설명적 이름을 사용했고,
docstring 에 간단한 함수 호출 결과를 추가했다.
"""
def divide_by_seven(n):
    return n  % 7 == 0

def has_seven_char(n):
    # print("tracking n: ", n)
    if n % 10 == 7:
        return True
    elif n < 10:
        return False
    else:
        return has_seven_char(n // 10)

def pingpong_bouncing_condition(n):
    return divide_by_seven(n) or has_seven_char(n)

def pingpong_bounce(n):
    """
    >>> pingpong_bounce(20)
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    """
    return [1 * pingpong_bouncing_condition(i) for i in range(1, n+1)]
    
def pingpong_bounce_count(n):
    """
    >>> pingpong_bounce_count(20)
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
    """
    return [sum(steps) for steps in [pingpong_bounce(k) for k in range(1,n+1)]]

def pingpong_steps(n):
    """ 각 원소에서 다음 원소에 추가되는 증가분(step)을 계산했다.
        증가 방향이 바뀌는 바운싱 횟수가 짝수이면 +1 이 증가분이고
        홀수이면 -1 이 증가분인 사실을 사용했다.
    >>> pingpong_steps(20)
    [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1]
    """
    return [1 if k % 2 == 0 else -1 for k in pingpong_bounce_count(n)]

def pingpong(n):
    """
    >>> pingpong(1)
    1
    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    """
    return sum(pingpong_steps(n-1)) + 1

def doctest():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    import unittest

    class TestPingpongFunctions(unittest.TestCase):
        
        def test_divide_by_seven(self):
            self.assertTrue(divide_by_seven(0))
            self.assertTrue(divide_by_seven(7))
            self.assertTrue(divide_by_seven(-7))
            self.assertTrue(divide_by_seven(154))
            
            self.assertFalse(divide_by_seven(6))
            self.assertFalse(divide_by_seven(-6))
            self.assertFalse(divide_by_seven(-1))

        def test_has_seven_char(self):
            self.assertTrue(has_seven_char(7))
            self.assertTrue(has_seven_char(17))
            self.assertTrue(has_seven_char(107))
            self.assertTrue(has_seven_char(178))
            self.assertTrue(has_seven_char(718))
            self.assertTrue(has_seven_char(777))

            self.assertFalse(has_seven_char(0))
            self.assertFalse(has_seven_char(6))
            self.assertFalse(has_seven_char(123))

        def test_pingpong_main(self):
            self.assertEqual(pingpong(1), 1)
            self.assertEqual(pingpong(7), 7)
            self.assertEqual(pingpong(8), 6)
            self.assertEqual(pingpong(68), 2)
            self.assertEqual(pingpong(100), 2)

    unittest.main(verbosity=2)

    doctest()

