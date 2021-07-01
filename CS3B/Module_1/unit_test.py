import unittest
import currency_converter as cc

class TestCC(unittest.TestCase): #WE are writing our own custom test class, in parentheses name of class we want to inherit from

    def test_bad_currencies(self):
        with self.assertRaises(KeyError): #we are claiming that this function should raise a certain error i.e keyerror
            cc.currency_converter(10, "AQW", "NZD")
        with self.assertRaises(KeyError): #we are claiming that this function should raise a certain error i.e keyerror
            cc.currency_converter(10, "NZD", "AQW")

    def test_non_positive_qty(self):
        with self.assertRaises(KeyError): #we are claiming that this function should raise a certain error i.e keyerror
            cc.currency_converter(-1, "NZD", "USD")

    def test_return_value(self):
        self.assertEqual(8, cc.currency_converter(10, 'USD', "GBP"))
        self.assertEqual(.71, cc.currency_converter(10, 'CAD', "USD"))
        self.assertEqual(8, cc.currency_converter(10, 'EUR', "USD"))

if __name__ == "__main__":
    unittest.main()

