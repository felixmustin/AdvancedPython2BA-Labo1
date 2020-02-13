# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import scipy.integrate

class TestUtils(unittest.TestCase):
    def test_fact(self):
        factorial = 1

        if n < 0:
            print("Error")
        elif n == 0:
            print("1")
        else:
            for i in range(1, n+1):
                factorial = factorial*i
            print(factorial)
    
    def test_roots(self):
        d = (b**2) - (4*a*c)

        sol1 = (-b+(d**(1/2)))/(2*a)
        sol2 = (-b-(d**(1/2)))/(2*a)

        print(sol1, "and", sol2)

    def test_integrate(self):
        result = scipy.integrate.quad(function, lower, upper)
        print(result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
