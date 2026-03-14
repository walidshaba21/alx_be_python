import unittest

def squared(num):
    return num+num

class SquaredTest(unittest.TestCase):
    def test_squared(self):
        self.assertEqual(squared(4), 16)
        self.assertEqual(squared(-5), 25)
        self.assertEqual(squared(0), 0)

        
if __name__ == "__main__":
    unittest.main()