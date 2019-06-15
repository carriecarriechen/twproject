import unittest
from index import*


class MyTest(unittest.TestCase):  # 继承unittest.TestCase

    def test_next_status(self):
        self.assertEqual(next_status([[1,1,1],[1,0,1],[0,1,0]]),[[1,0,0],[1,0,0],[0,0,0]])

if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例