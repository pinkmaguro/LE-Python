from unittest import TestCase
from unittest.mock import patch, Mock
import main
from main import Calculator, Blog


class TestCalculator(TestCase):
    """ 애플리케이션의 클래스를 직접 테스트 하는 경우 """
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.sum(2,4), 6)

class TestCalculator2(TestCase):
    """ Patch 의 타겟에이 MagicMock 으로 대체된다. (new=DEFAULT) 인 경우"""
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)

class TestCalculator3(TestCase):
    @patch('main.Calculator.sum')
    def test_sum(self, sum):
        sum.return_value = 8
        self.assertEqual(sum(2,3), 8)

class TestCalculator4(TestCase):
    """ mock 클래스의 메쏘드를 여러번 호출하는 경우에는
        side_effect 를 사용한다. """
    @patch('main.Calculator.sum', side_effect=[100])
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 100)

def mock_sum(a, b):
    return a + b

class TestCalculator5(TestCase):
    """ 타겟 메쏘드의 역할을 다른 함수에게 위임할 수 있다."""
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)


class TestBlog(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # Additional assertions
        assert MockBlog is main.Blog # The mock is equivalent to the original

        assert MockBlog.called # The mock wasP called

        blog.posts.assert_called_with() # We called the posts method with no arguments

        blog.posts.assert_called_once_with() # We called the posts method once with no arguments

        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments

        blog.reset_mock() # Reset the mock object

        blog.posts.assert_not_called() # After resetting, posts has not been called.