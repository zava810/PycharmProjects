import unittest
import fibonacci


class test_fibonacci(unittest.TestCase):
    def test_ziro(self):
        with self.assertRaises(ValueError):
            fibonacci.get_fib_list(2)


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "6 hona chahiye")


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_inlist(self):
        li = [2, 5, 4]
        self.assertIn(6, li, 'element list me nhi h')


if __name__ == '__main__':
    unittest.main()
