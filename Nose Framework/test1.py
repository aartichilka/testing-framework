from nose.tools import assert_equals

from nose import with_setup  # optional

def setup_module(module):
    print("")  # this is to get a newline after the dots
    print("setup_module before anything in this file")


def teardown_module(module):
    print("teardown_module after everything in this file")


def multiply(x,y):
    return x * y

class TestUM:

    def setup(self):
        print("TestUM:setup() before each test method")

    def teardown(self):
        print("TestUM:teardown() after each test method")

    @classmethod
    def setup_class(cls):
        print("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class() after any methods in this class")

    def test_numbers_5_6(self):
        print('test_numbers_5_6()  <============================ actual test code')
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print('test_strings_b_2()  <============================ actual test code')
        assert multiply('b', 2) == 'bb'