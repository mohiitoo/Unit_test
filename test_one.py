import unittest
import one

class one_test(unittest.TestCase):
    
    def test_Sum(self):
        self.assertEqual(one.Sum(5, 6), 11)

    def test_Subtraction(self):
        self.assertEqual(one.Subtraction(10,3), 7)

    def test_Multiplication(self):
        self.assertEqual(one.Multiplication(2, 5),10)

    def test_Division(self):
        self.assertEqual(one.Division(100, 5), 20)
        self.assertRaises(ZeroDivisionError, one.Division ,5, 0 )

if __name__== '__main__':
    unittest.main()