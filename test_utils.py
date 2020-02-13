# test_utils.py

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(2), 2)
        self.assertEqual(utils.fact(0), 1)
        with self.assertRaises(ValueError):
            utils.fact(-1)
    def test_roots(self):
        self.assertEqual(utils.roots(-1, 0, 1), (-1, 1))
        self.assertEqual(utils.roots(1, -4, 4), (2))
    def test_integrate(self):
        self.assertAlmostEqual(utils.integrate("2*x", -4, 2), -12)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
