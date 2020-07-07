
import unittest

def add(x,y):
    return x+y

class test(unittest.TestCase):

    @unittest.skip("demonstrating skip")
    def test_Add(self):
        self.assertEquals(add(4,5),9)

if __name__ == '__main__':
    unittest.main()