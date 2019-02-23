import unittest
import os
import sys

sys.path.append(os.path.dirname(__file__))
from singleton import Singleton

class TestSingleton(unittest.TestCase):
    """Singleton __new__ テスト
    """

    def test___new__(self):
        a = Singleton()
        b = Singleton()
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
