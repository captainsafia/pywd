import unittest
from pywd.pywd import create_password

class TestPywd(unittest.TestCase):
    def setUp(self):
        self.length = 10

    def test_n(self):
        password = create_password(self.length, True, False, False, False)
        self.assertTrue(password.isdigit())
    
    def test_l(self):
        password = create_password(self.length, False, True, False, False)
        self.assertTrue(password.isalpha())

    def test_u(self):
        password = create_password(self.length, False, True, False, True)
        self.assertTrue(password.isalpha() and any([x.isupper() for x in password]))

    def test_s(self):
        password = create_password(self.length, False, False, True, False)
        self.assertFalse(password.isalnum())

if __name__ == '__main__':
    unittest.main()
