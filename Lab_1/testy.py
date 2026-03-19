import unittest
from main import Add

class MyTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(Add(""), 0)
    def test_one(self):
        self.assertEqual(Add("1"), 1)
    def test_twosum(self):
        self.assertEqual(Add("1,2"), 3)
    def test_wiele(self):
            self.assertEqual(Add("1,2,3"), 6)
    def test_error(self):
            with self.assertRaises(ValueError):
                Add("b,\n")
    def test_nline(self):
        self.assertEqual(Add("1\n2,3"),6)
    def test_nlineerror(self):
        with self.assertRaises(ValueError):
            Add("1,\n2,3")

if __name__ == '__main__':
    unittest.main()

