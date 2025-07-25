import unittest
from indian_currency_format import indian_currency_format

class TestIndianCurrencyFormat(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(indian_currency_format(123456.7891), "1,23,456.7891")
        self.assertEqual(indian_currency_format(1234567890.12), "1,23,45,67,890.12")
        self.assertEqual(indian_currency_format(-9876543.21), "-98,76,543.21")

    def test_small_numbers(self):
        self.assertEqual(indian_currency_format(12.34), "12.34")
        self.assertEqual(indian_currency_format(0.1234), "0.1234")
        self.assertEqual(indian_currency_format(123), "123")
        self.assertEqual(indian_currency_format(-123), "-123")

    def test_edge_cases(self):
        self.assertEqual(indian_currency_format(1000), "1,000")
        self.assertEqual(indian_currency_format(100000), "1,00,000")
        self.assertEqual(indian_currency_format(0), "0")
        self.assertEqual(indian_currency_format(-0.0), "-0.0")
        self.assertEqual(indian_currency_format(.25), "0.25")

    def test_large_numbers(self):
        # Pass the large number as string to preserve decimal precision
        self.assertEqual(indian_currency_format("123456789012345.6789"), "12,34,56,78,90,12,345.6789")

    def test_no_decimal(self):
        self.assertEqual(indian_currency_format(10000000), "1,00,00,000")
        self.assertEqual(indian_currency_format(-10000000), "-1,00,00,000")


if __name__ == '__main__':
    unittest.main()
