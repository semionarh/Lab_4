import unittest

from rational_number import RationalNum, rationalization


class TestMethodsArithmetic(unittest.TestCase):

    def test_true_value1(self):
        self.assertTrue(RationalNum(1, 5))
        self.assertTrue(RationalNum(0, 5))
        self.assertTrue(RationalNum(-1, 5))
        self.assertTrue(RationalNum(1, -5))
        self.assertTrue(RationalNum(-1, -5))

    def test_wrong_value(self):
        with self.assertRaises(IOError):
            RationalNum(2, 0)
        with self.assertRaises(IOError):
            RationalNum(0, 0)
        with self.assertRaises(IOError):
            RationalNum(1.2, 2)
        with self.assertRaises(IOError):
            RationalNum(1, 1.2)

    def test_add(self):
        self.assertEqual(RationalNum(1, 1) + RationalNum(1, 1), RationalNum(2, 1))
        self.assertEqual(RationalNum(-1, 1) + RationalNum(1, 1), RationalNum(0, 1))
        self.assertEqual(RationalNum(1, -1) + RationalNum(1, 1), RationalNum(0, 1))
        self.assertEqual(RationalNum(-1, 1) + RationalNum(1, -1), RationalNum(-2, 1))
        self.assertEqual(RationalNum(0, 1) + RationalNum(0, 1), RationalNum(0, 1))
        self.assertEqual(RationalNum(55432, 55) + RationalNum(789, 4), RationalNum(265123, 220))

    def test_sub(self):
        self.assertEqual(RationalNum(1, 1) - RationalNum(1, 1), RationalNum(0, 1))
        self.assertEqual(RationalNum(-1, 1) - RationalNum(1, 1), RationalNum(-2, 1))
        self.assertEqual(RationalNum(1, -1) - RationalNum(1, 1), RationalNum(-2, 1))
        self.assertEqual(RationalNum(1, 1) - RationalNum(1, -1), RationalNum(2, 1))
        self.assertEqual(RationalNum(0, 1) - RationalNum(1, 1), RationalNum(-1, 1))
        self.assertEqual(RationalNum(55432, 55) - RationalNum(789, 4), RationalNum(178333, 220))

    def test_mul(self):
        self.assertEqual(RationalNum(1, 1) * RationalNum(1, 1), RationalNum(1, 1))
        self.assertEqual(RationalNum(2, 3) * RationalNum(2, 1), RationalNum(4, 3))
        self.assertEqual(RationalNum(-2, 3) * RationalNum(-2, 1), RationalNum(4, 3))
        self.assertEqual(RationalNum(2, -3) * RationalNum(2, 1), RationalNum(-4, 3))
        self.assertEqual(RationalNum(0, 3) * RationalNum(2, 1), RationalNum(0, 3))
        self.assertEqual(RationalNum(55432, 55) * RationalNum(789, 4), RationalNum(43735848, 220))

    def test_truediv(self):  # /
        self.assertEqual(RationalNum(1, 1) / RationalNum(1, 1), RationalNum(1, 1))
        self.assertEqual(RationalNum(2, 1) / RationalNum(-2, 1), RationalNum(-2, 2))
        self.assertEqual(RationalNum(6, 3) / RationalNum(3, 4), RationalNum(24, 9))
        with self.assertRaises(ZeroDivisionError):
            RationalNum(5, 1) / RationalNum(0, 1)
        self.assertEqual(RationalNum(55432, 55) / RationalNum(789, 4), RationalNum(221728, 43395))

    def test_floordiv(self):  # div
        self.assertEqual(RationalNum(1, 1) // RationalNum(1, 1), 1)
        self.assertEqual(RationalNum(2, 1) // RationalNum(-2, 1), -1)
        self.assertEqual(RationalNum(8, 3) // RationalNum(3, 4), 3)
        self.assertEqual(RationalNum(8, 3) // RationalNum(3, -4), -4)
        with self.assertRaises(ZeroDivisionError):
            RationalNum(5, 1) // RationalNum(0, 1)
        self.assertEqual(RationalNum(789, 4) // RationalNum(432, 55), 25)

    def test_mod(self):
        self.assertEqual(RationalNum(1, 1) % RationalNum(1, 1), 0)
        self.assertEqual(RationalNum(2, 1) % RationalNum(-2, 1), 0)
        self.assertEqual(RationalNum(8, 3) % RationalNum(3, 4), 5)
        self.assertEqual(RationalNum(8, 3) % RationalNum(3, -4), -4)
        with self.assertRaises(ZeroDivisionError):
            RationalNum(5, 1) % RationalNum(0, 1)
        self.assertEqual(RationalNum(789, 4) % RationalNum(432, 55), 195)

    def tests_compare(self):
        self.assertTrue(RationalNum(54, 2) == RationalNum(108, 4))
        self.assertTrue(RationalNum(54, 2) != RationalNum(104, 4))
        self.assertTrue(RationalNum(54, 2) <= RationalNum(108, 4))
        self.assertTrue(RationalNum(54, 2) >= RationalNum(104, 4))
        self.assertTrue(RationalNum(3, 2) > RationalNum(2, 3))
        self.assertFalse(RationalNum(3, 2) < RationalNum(2, 3))


class TestMethodsReduction(unittest.TestCase):
    def test_1(self):
        a = RationalNum(2, 2)
        a.abbreviation()
        self.assertEqual(a, RationalNum(1, 1))

    def test_2(self):
        a = RationalNum(145325, 55)
        a.abbreviation()
        self.assertEqual(a, RationalNum(29065, 11))

    def test_3(self):
        a = RationalNum(0, 55)
        a.abbreviation()
        self.assertEqual(a, RationalNum(0, 55))

    def test_4(self):
        a = RationalNum(111, 55)
        a.abbreviation()
        self.assertEqual(a, RationalNum(111, 55))


class TestMethodsConvert(unittest.TestCase):
    def test_to_decimal(self):
        self.assertEqual(RationalNum(4, 27).decimalisation(), "0.(148)")
        self.assertEqual(RationalNum(3, 27).decimalisation(), "0.(1)")
        self.assertEqual(RationalNum(-7, 27).decimalisation(), "-0.(259)")
        self.assertEqual(RationalNum(183498, 36).decimalisation(), "5097.1(6)")
        self.assertEqual(RationalNum(1, 3).decimalisation(), "0.(3)")
        self.assertEqual(RationalNum(5, -3).decimalisation(), "-1.(6)")
        self.assertEqual(RationalNum(-5, 5).decimalisation(), "-1.0")
        self.assertEqual(RationalNum(3870, 36).decimalisation(), "107.5")
        self.assertEqual(RationalNum(0, 36).decimalisation(), "0.0")
        with self.assertRaises(IOError):
            RationalNum(36, 0).decimalisation()

    def test_to_rational(self):
        self.assertEqual(rationalization("0.(148)"), RationalNum(4, 27))
        self.assertEqual(rationalization("0.(1)"), RationalNum(3, 27))
        self.assertEqual(rationalization("-0.(259)"), RationalNum(-7, 27))
        self.assertEqual(rationalization("5097.1(6)"), RationalNum(91747, 18))
        self.assertEqual(rationalization("0.(3)"), RationalNum(1, 3))
        self.assertEqual(rationalization("-1.(6)"), RationalNum(5, -3))
        self.assertEqual(rationalization("-1.0"), RationalNum(-5, 5))
        self.assertEqual(rationalization("107.5"), RationalNum(3870, 36))
        self.assertEqual(rationalization("0.0"), RationalNum(0, 1))
        self.assertEqual(rationalization("0.1"), RationalNum(1, 10))
        self.assertEqual(rationalization("5.27"), RationalNum(527, 100))


if __name__ == '__main__':
    unittest.main()
