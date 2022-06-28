import unittest
from new_enum import NewEnum

class Test(NewEnum):
    test1 = "test1_value"
    test2 = "test2_value"
    test3 = "test3_value"

    def func1(cls):
        return "func1"
    def func2(cls):
        return "func2"

class TestNewEnum(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(Test.test1, "test1")

    def test_get_enum_values(self):
        self.assertEqual(Test.get_values(),["test1_value", "test2_value", "test3_value"])

    def test_get_enum_names(self):
        self.assertEqual(Test.get_names(),["test1", "test2", "test3"])

    def test_get_enum_functions(self):
        functions = Test.get_functions()
        for i, func in enumerate(functions):
            self.assertEqual(func(Test), "func"+str(i+1))
