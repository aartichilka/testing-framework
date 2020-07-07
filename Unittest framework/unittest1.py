# unit test

import unittest

class sample(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            print("calls once before any tests in class")

        @classmethod
        def tearDownClass(cls):
            print("calls once after all tests in class")

        def setUp(self):
            self.a  = 10
            self.b = 20

        def tearDown(self):
            print("end of test caese")


        def test_add(self):
            res = self.a + self.b
            self.assertTrue(res == 30)

