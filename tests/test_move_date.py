import datetime
import unittest

from move_date import util


class TestStringMethods(unittest.TestCase):

    def test_move_date_2(self):
        d = util.date2()
        self.assertEqual(d, 'stub2')
        pass

    def test_move_backward_days(self):
        d1 = datetime.date(2016, 6, 25)
        d2 = util.move_backward_days(d1, 3)
        exp = datetime.date(2016, 6, 22)
        self.assertEqual(exp, d2)

    def test_move_backward_days2(self):
        d1 = datetime.date(2016, 3, 1)
        d2 = util.move_backward_days(d1, 3)
        exp = datetime.date(2016, 2, 27)
        self.assertEqual(exp, d2)

    def test_move_backward_weeks(self):
        d1 = datetime.date(2016, 3, 25)
        d2 = util.move_backward_weeks(d1, 4)
        exp = datetime.date(2016, 2, 26)
        self.assertEqual(exp, d2)

    def test_move_backward_months(self):
        d1 = datetime.date(2016, 3, 31)
        d2 = util.move_backward_months(d1, 3)
        exp = datetime.date(2015, 12, 31)
        self.assertEqual(exp, d2)

    def test_move_backward_months2(self):
        d1 = datetime.date(2016, 3, 31)
        d2 = util.move_backward_months(d1, 2)
        exp = datetime.date(2016, 1, 31)
        self.assertEqual(exp, d2)

    def test_move_backward_months3(self):
        d1 = datetime.date(2016, 3, 13)
        d2 = util.move_backward_months(d1, 3)
        exp = datetime.date(2015, 12, 13)
        self.assertEqual(exp, d2)

    def test_move_backward_months4(self):
        d1 = datetime.date(2016, 4, 30)
        d2 = util.move_backward_months(d1, 2)
        exp = datetime.date(2016, 2, 29)
        self.assertEqual(exp, d2)

    def test_move_backward_months5(self):
        d1 = datetime.date(2017, 1, 13)
        d2 = util.move_backward_months(d1, 1)
        exp = datetime.date(2016, 12, 13)
        self.assertEqual(exp, d2)

    def test_move_backward_months6(self):
        d1 = datetime.date(2019, 1, 13)
        d2 = util.move_backward_months(d1, 25)
        exp = datetime.date(2016, 12, 13)
        self.assertEqual(exp, d2)

    def test_move_backward_months7(self):
        d1 = datetime.date(2019, 2, 28)
        d2 = util.move_backward_months(d1, 26)
        exp = datetime.date(2016, 12, 28)
        self.assertEqual(exp, d2)

    def test_move_backward_months8(self):
        d1 = datetime.date(2016, 2, 29)
        d2 = util.move_backward_months(d1, 24)
        exp = datetime.date(2014, 2, 28)
        self.assertEqual(exp, d2)

    def test_move_forward_days(self):
        d1 = datetime.date(2016, 6, 25)
        d2 = util.move_forward_days(d1, 3)
        exp = datetime.date(2016, 6, 28)
        self.assertEqual(exp, d2)

    def test_move_forward_weeks(self):
        d1 = datetime.date(2016, 3, 25)
        d2 = util.move_forward_weeks(d1, 3)
        exp = datetime.date(2016, 4, 15)
        self.assertEqual(exp, d2)

    def test_move_forward_months(self):
        d1 = datetime.date(2016, 3, 31)
        d2 = util.move_forward_months(d1, 3)
        exp = datetime.date(2016, 6, 30)
        self.assertEqual(exp, d2)

    def test_move_forward_months2(self):
        d1 = datetime.date(2016, 3, 31)
        d2 = util.move_forward_months(d1, 2)
        exp = datetime.date(2016, 5, 31)
        self.assertEqual(exp, d2)

    def test_move_forward_months3(self):
        d1 = datetime.date(2016, 3, 13)
        d2 = util.move_forward_months(d1, 3)
        exp = datetime.date(2016, 6, 13)
        self.assertEqual(exp, d2)

    def test_move_forward_months4(self):
        d1 = datetime.date(2016, 3, 13)
        d2 = util.move_forward_months(d1, 2)
        exp = datetime.date(2016, 5, 13)
        self.assertEqual(exp, d2)

    def test_move_forward_months5(self):
        d1 = datetime.date(2016, 12, 13)
        d2 = util.move_forward_months(d1, 1)
        exp = datetime.date(2017, 1, 13)
        self.assertEqual(exp, d2)

    def test_move_forward_months6(self):
        d1 = datetime.date(2016, 12, 13)
        d2 = util.move_forward_months(d1, 25)
        exp = datetime.date(2019, 1, 13)
        self.assertEqual(exp, d2)

    def test_move_forward_months7(self):
        d1 = datetime.date(2016, 12, 31)
        d2 = util.move_forward_months(d1, 26)
        exp = datetime.date(2019, 2, 28)
        self.assertEqual(exp, d2)

    def test_move_forward_years(self):
        d1 = datetime.date(2016, 3, 13)
        d2 = util.move_forward_years(d1, 2)
        exp = datetime.date(2018, 3, 13)
        self.assertEqual(exp, d2)

    def test_move_forward_years2(self):
        d1 = datetime.date(2016, 2, 29)
        d2 = util.move_forward_years(d1, 2)
        exp = datetime.date(2018, 2, 28)
        self.assertEqual(exp, d2)

    def test_move_forward_years3(self):
        d1 = datetime.date(2016, 2, 12)
        d2 = util.move_forward_years(d1, 2)
        exp = datetime.date(2018, 2, 12)
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

