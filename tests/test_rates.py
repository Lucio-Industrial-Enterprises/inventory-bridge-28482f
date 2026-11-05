import unittest

from warehouse.rates import shipping_quote


class StandardRateTests(unittest.TestCase):
    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")


class ExpressRateTests(unittest.TestCase):
    def test_express_local(self):
        # express adds $7 flat surcharge: 5.0 + 1.5*2 + 7 = 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # express adds $7 flat surcharge: 8.0 + 1.5*2 + 7 = 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # 5.0 + 1.5*1.5 + 7 = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
