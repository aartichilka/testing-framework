import unittest
import math
import re

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertAlmostEqual(22/7,3.14,places=2)
   def test2(self):
      self.assertNotAlmostEqual(10/3,3.33)
   def test3(self):
      self.assertGreater(math.pi,3)
   def test4(self):
      #self.assertRegexpMatches("Tutorials Point (I) Private Limited","Point")
      self.assertRegex("Tutorials Point (I) Private Limited","Point")

if __name__ == '__main__':
   unittest.main()