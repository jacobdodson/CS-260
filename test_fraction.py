import unittest
from fractionClass import Fraction

class test_fraction(unittest.TestCase):
    """Unit test class for Fractin class"""
    def test_add(self):

        frac = Fraction(1,2)

        self.assertEqual(str(frac + Fraction(1,2)), str(Fraction(1,1)))
        self.assertEqual(str(frac + Fraction(1,3)), str(Fraction(5,6)))
        self.assertEqual(str(frac + Fraction(-1,2)), str(Fraction(0,4)))
        self.assertEqual(str(frac + Fraction(1,-2)), str(Fraction(0,-4)))
        self.assertEqual(str(frac + Fraction(-1,-2)), str(Fraction(-1,-1)))

    def test_subtract(self):

        frac = Fraction(1,2)
        
        self.assertEqual(str(frac - Fraction(1,2)), str(Fraction(0,4)))
        self.assertEqual(str(frac - Fraction(1,3)), str(Fraction(1,6)))
        self.assertEqual(str(frac - Fraction(-1,2)), str(Fraction(1,1)))
        self.assertEqual(str(frac - Fraction(1,-2)), str(Fraction(-1,-1)))
        self.assertEqual(str(frac - Fraction(-1,-2)), str(Fraction(0,-4)))

    def test_multiply(self):
        
        frac = Fraction(1,2)
        
        self.assertEqual(str(frac * Fraction(1,2)), str(Fraction(1,4)))
        self.assertEqual(str(frac * Fraction(1,3)), str(Fraction(1,6)))
        self.assertEqual(str(frac * Fraction(-1,2)), str(Fraction(-1,4)))
        self.assertEqual(str(frac * Fraction(1,-2)), str(Fraction(1,-4)))
        self.assertEqual(str(frac * Fraction(-1,-2)), str(Fraction(-1,-4)))

    def test_divide(self):
    
        frac = Fraction(1,2)
        
        self.assertEqual(str(frac / Fraction(1,2)), str(Fraction(1,1)))
        self.assertEqual(str(frac / Fraction(1,3)), str(Fraction(3,2)))
        self.assertEqual(str(frac / Fraction(-1,2)), str(Fraction(1,-1)))
        self.assertEqual(str(frac / Fraction(1,-2)), str(Fraction(-1,1)))
        self.assertEqual(str(frac / Fraction(-1,-2)), str(Fraction(-1,-1)))
"""
    def test_gcd(self):
        self.assertEqual(frac.gcd(1/2, 1/3), 6)
"""
        

if __name__ == '__main__':
    unittest.main()
