
import unittest

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertListEqual([2,3,4], [2,3,4])
   def test2(self):
      self.assertTupleEqual((1*2,2*2,3*2), (2,4,6))
   def test3(self):
      self.assertDictEqual({1:11,2:22,3:33},{3:33,2:22,1:11})

if __name__ == '__main__':
   unittest.main()