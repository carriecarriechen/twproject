import unittest
from index import*
from unittest.mock import patch


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    '''
    def test_print2d(self):
        self.assertEqual(print2d([[1,1,1],[1,0,1],[0,1,0]]),)
    这是一个没有Return的函数
    def test_init2d(self):
        self.assertEqual(init2d())
    这是一个无输入且有无限种输出的函数
    def test_iteration(self):
        self.assertEqual()
    这是迭代N代，手工推演结果很复杂。。
    '''
    def test_next_status(self):
        self.assertEqual(next_status([[1,1,1],[1,0,1],[0,1,0]]),[[1,0,0],[1,0,0],[0,0,0]])



if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例