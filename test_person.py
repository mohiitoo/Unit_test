import unittest
import person


class persontesst(unittest.TestCase):
    
    def setUp(self):
        self.i1 = person.person('mmad' ,'alizadeh')
        self.i2 = person.person('naser' ,'jabari')

    def test_fullname(self):
        self.assertEqual(self.i1.fullname(),'mmad alizadeh')
        self.assertEqual(self.i2.fullname(),'naser jabari')

    def test_eamil(self):
        self.assertEqual(self.i1.email(),'mmadalizadeh@gmail.com')
        self.assertEqual(self.i2.email(),'naserjabari@gmail.com')

if __name__ == '__main__':
    unittest.main()