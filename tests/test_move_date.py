import datetime
import unittest

from move_date import util


class TestStringMethods(unittest.TestCase):

    def test_move_date_2(self):
        d = util.date2()
        self.assertEqual(d, 'stub2')
        pass

    def test_move_forward_days(self):
        d1 = datetime.datetime(2016, 6, 25, 22, 55, 58)
        d2 = util.move_forward_days(d1, 3)
        exp = datetime.datetime(2016, 6, 28, 22, 55, 58)
        self.assertEqual(exp, d2)

    def test_move_forward_weeks(self):
        d1 = datetime.datetime(2016, 3, 25, 22, 55, 58)
        d2 = util.move_forward_weeks(d1, 3)
        exp = datetime.datetime(2016, 4, 15, 22, 55, 58)
        self.assertEqual(exp, d2)

    def test_move_forward_months(self):
        d1 = datetime.datetime(2016, 3, 31, 22, 55, 58)
        d2 = util.move_forward_months(d1, 3)
        exp = datetime.datetime(2016, 6, 30, 22, 55, 58)
        self.assertEqual(exp, d2)

    def test_move_forward_months2(self):
        d1 = datetime.datetime(2016, 3, 31, 22, 55, 58)
        d2 = util.move_forward_months(d1, 2)
        exp = datetime.datetime(2016, 5, 31, 22, 55, 58)
        self.assertEqual(exp, d2)

    def test_move_forward_months3(self):
        d1 = datetime.datetime(2016, 3, 13, 22, 55, 58)
        d2 = util.move_forward_months(d1, 3)
        exp = datetime.datetime(2016, 6, 13, 22, 55, 58)
        self.assertEqual(exp, d2)

    def test_move_forward_months4(self):
        d1 = datetime.datetime(2016, 3, 13, 22, 55, 58)
        d2 = util.move_forward_months(d1, 2)
        exp = datetime.datetime(2016, 5, 13, 22, 55, 58)
        self.assertEqual(exp, d2)

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

if __name__ == '__main__':
    unittest.main()

