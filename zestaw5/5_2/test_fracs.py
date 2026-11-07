import unittest
import fracs

class TestFracs(unittest.TestCase):

    def setUp(self):
        self.frac = [
            [-1, 2],
            [1, -2],
            [0, 1],
            [0, 2],
            [3, 1],
            [6, 2],
            [3, 6],
            [1, 3]
        ]

    def test_minimize_fraction(self):
        for frac in self.frac:
            fracs.minimize_fraction(frac)

        self.assertEqual(self.frac[0], [-1, 2])
        self.assertEqual(self.frac[1], [-1, 2])
        self.assertEqual(self.frac[2], [0, 1])
        self.assertEqual(self.frac[3], [0, 1])
        self.assertEqual(self.frac[4], [3, 1])
        self.assertEqual(self.frac[5], [3, 1])
        self.assertEqual(self.frac[6], [1, 2])
        self.assertEqual(self.frac[7], [1, 3])

    def test_common_denominator(self):
        fracs.common_denominator(self.frac[6], self.frac[7])
        fracs.common_denominator(self.frac[0], self.frac[4])

        self.assertEqual(self.frac[6], [3, 6])
        self.assertEqual(self.frac[7], [2, 6])

        self.assertEqual(self.frac[0], [-1, 2])
        self.assertEqual(self.frac[4], [6, 2])

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac(self.frac[6], self.frac[7]), [5, 6])
        self.assertEqual(fracs.add_frac(self.frac[1], self.frac[3]), [-1, 2])
        self.assertEqual(fracs.add_frac(self.frac[0], self.frac[4]), [5, 2])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac(self.frac[6], self.frac[7]), [1, 6])
        self.assertEqual(fracs.sub_frac(self.frac[1], self.frac[3]), [-1, 2])
        self.assertEqual(fracs.sub_frac(self.frac[0], self.frac[4]), [-7, 2])

    def test_mul_frac(self):
        self.assertEqual(fracs.mult_frac(self.frac[6], self.frac[7]), [1, 6])
        self.assertEqual(fracs.mult_frac(self.frac[1], self.frac[3]), [0, 1])
        self.assertEqual(fracs.mult_frac(self.frac[0], self.frac[4]), [-3, 2])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac(self.frac[6], self.frac[7]), [3, 2])
        with self.assertRaises(ZeroDivisionError):
            fracs.div_frac(self.frac[1], self.frac[3])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive(self.frac[6]), True)
        self.assertEqual(fracs.is_positive(self.frac[1]), False)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero(self.frac[2]), True)
        self.assertEqual(fracs.is_zero(self.frac[6]), False)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac(self.frac[6], self.frac[7]), 1)
        self.assertEqual(fracs.cmp_frac(self.frac[1], self.frac[3]), -1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float(self.frac[6]), 0.5)
        self.assertEqual(fracs.frac2float(self.frac[1]), -0.5)
        self.assertAlmostEqual(fracs.frac2float(self.frac[7]), 0.33333, places = 5)

if __name__ == "__main__":
    unittest.main()