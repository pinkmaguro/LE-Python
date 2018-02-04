"""
파이썬  공식 문서(https://docs.python.org/3/library/unittest.mock.html)를 읽고
나름대로 이해한 내용을 정리합니다.

MagicMock 은 Mock 을 상속한 클래스로 매직메쏘드가 기본으로 지원됩니다.

# MagicMock
리턴 값을 지정한 mock 메쏘드를 만든다.

some_instance.some_method = MagicMock(return_value=3)


# 에러를 발생시키고 싶을 때는 
some_instance.some_method = Mock(side_effect=KeyError('foo'))

"""

from unittest.mock import MagicMock, Mock
from unittest.mock import patch
import unittest
import time


class Calculator:
    def sum(self, a, b):
        time.sleep(10) # long running process
        return a + b



class TestMock(unittest.TestCase):

    def test_magicmock(self):
        some_method = MagicMock(return_value=3)
        self.assertEqual(some_method(), 3)

    def test_error_situation(self):
        some_method = Mock(side_effect=KeyError('foo'))
        self.assertRaises(KeyError,some_method)

    def test_side_effect_is_list(self):
        some_method = Mock()
        some_method.side_effect = [1,3,2,4,5]
        self.assertListEqual([some_method(),
                              some_method(),
                              some_method(),
                              some_method(),
                              some_method()]   ,[1,3,2,4,5])
        # there is no return value to feed
        self.assertRaises(StopIteration, some_method)

    def test_side_effect_is_function(self):
        some_dict = {'a':1, 'b':2, 'c':3}
        def side_effect(arg):
            return some_dict[arg]
        some_method = Mock(side_effect=side_effect)
        self.assertEqual(some_method('a'),some_dict['a'])
        self.assertEqual(some_method('b'),some_dict['b'])
        self.assertEqual(some_method('c'),some_dict['c'])

    @patch('__main__.Calculator.sum')
    def test_calculator_sum(self, sum):
        Calculator.sum.return_value = 9
        self.assertEqual(sum(2,3), 9)

    def test_magicmock_support_matic_method(self):
        some_method = MagicMock()
        some_method.__str__.return_value = 'foobarbaz'
        self.assertEqual(str(some_method), 'foobarbaz')
        # 아래의 테스트를 unittest 의 assert 로 테스트할 수 없을까?  디자인이 마음에 안 든다.
        some_method.__str__.assert_called_with()

    def test_patch_with_context_manager(self):
        with patch.object(Calculator, 'sum', return_value=9) as mock_method:
            calc = Calculator()
            calc.sum(1,2)
            mock_method.assert_called_with(1,2)

    def test_patch_dict(self):
        foo = {'key': 'value'}
        original = foo.copy()
        with patch.dict(foo, {'newkey':'newvalue'}, clear=True):
            self.assertTrue(foo == {'newkey':'newvalue'})
        # 컨텍스트 밖에서는 foo 는 원래의 값으로 돌아간다.
        self.assertTrue(foo == original)

        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)