import unittest
import math

def sign(value):
    if value < 0:
        return -1
    else:
        return 1
    
class TestSign(unittest.TestCase):
    def test_sign_negative(self):
        self.assertEqual(-1, sign(-3))

    def test_sign_positive(self):
        self.assertEqual(1, sign(19))

    def test_sign_zero(self):
        self.assertEqual(1, sign(0))

    def test_sign_error(self):
        with self.assertRaises(TypeError):
            sign('one')

if __name__=='__main__':
	unittest.main()