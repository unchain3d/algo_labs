import unittest
from src.rabin_karp_algo import rabin_karp_algo


class MyTestCase(unittest.TestCase):
    def test_1(self):
        haystack = ""
        needle = ""
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([], result)

    def test_2(self):
        haystack = "a"
        needle = "a"
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([0], result)

    def test_3(self):
        haystack = "word"
        needle = "word"
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([0], result)

    def test_4(self):
        haystack = "adefinitelyreallyverysupermegalongmaybeeveninfinitestring"
        needle = "really"
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([11], result)

    def test_5(self):
        haystack = "quitetheroomyroomyouhaveinthisenormouslybigroom"
        needle = "room"
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([8, 13, 43], result)

    def test_6(self):
        haystack = "numberslike1234567891011"
        needle = "1"
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([11, 20, 22, 23], result)

    def test_7(self):
        haystack = "Your Room Number Is 404"
        needle = "Is"
        result = rabin_karp_algo(haystack, needle)
        print(f"Вхідні індекси {needle}, що знаходяться в {haystack}: {result}")
        self.assertEqual([17], result)


if __name__ == "__main__":
    unittest.main()
