import unittest

class sample(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            print("calls once before any tests in class")

        @classmethod
        def tearDownClass(cls):
            print("calls once after all tests in class")

        def setUp(self):
            self.a  = 20
            self.b = 10

        def tearDown(self):
            print("end of test case")


        def test_add(self):
            res = self.a + self.b
            self.assertTrue(res == 30)

        def test_sub(self):
            res = self.a - self.b
            self.assertTrue(res == 10)

if __name__ == '__main__' :

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(sample))

    runner = unittest.TextTestRunner()

    runner.run(suite)

