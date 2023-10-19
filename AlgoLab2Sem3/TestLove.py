import unittest
from love import love


class TestLove(unittest.TestCase):
    def test_love_1(self):
        P = 12
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = True
        self.assertEqual(love(numbers, P), expected)

    def test_love_2(self):
        P = 34
        numbers = [1, 5, 10, 20, 100, 200, 500, 1000]
        expected = False
        self.assertEqual(love(numbers, P), expected)

    def test_love_3(self):
        P = 48
        numbers = [12, 15, 33, 0, 65]
        expected = True
        self.assertEqual(love(numbers, P), expected)

    def test_love_4(self):
        P = 35
        numbers = [5, 7, 10, 14, 23, 37, 101]
        expected = True
        self.assertEqual(love(numbers, P), expected)

    def test_love_5(self):
        P = 20
        numbers = [12, 6, 7, 10, 20, 30, 5, 4, 15, 1]
        expected = True
        self.assertEqual(love(numbers, P), expected)

#    def test_love_6(self):
#        P = 1
#        numbers = [16, 32, 67, 100, -15, 21, 1100, 23, 44, 99, 201, 22, 0]
#        expected = True
#        self.assertEqual(love(numbers, P), expected)

#    def test_love_7(self):
#        P = 60
#        numbers = [10, 20, 20, 20]
#        expected = True
#        self.assertEqual(love(numbers, P), expected)


if __name__ == '__main__':
    unittest.main()
