import unittest

import currency_converter as cc
import load_file_extra_credit as lf


class TestCC(unittest.TestCase):

    def test_bad_currencies(self):
        with self.assertRaises(KeyError):
            cc.CurrencyConverter(10, "AQW", "NZD")
        with self.assertRaises(KeyError):
            cc.CurrencyConverter(10, "NZD", "AQW")

    def test_non_positive_qty(self):
        with self.assertRaises(KeyError):
            cc.CurrencyConverter(-1, "NZD", "USD")

    def test_return_values(self):
        self.assertEqual(8, cc.CurrencyConverter(10, "USD", "GBP"))
        self.assertEqual(8, cc.CurrencyConverter(1, "CAD", "USD"))
        self.assertEqual(8, cc.CurrencyConverter(10, "EUR", "USD"))

    def test_lines_of_airbnb_data(self):
        self.assertEqual(48895, lf.load_file())


if __name__ == '__main__':
    unittest.main()
