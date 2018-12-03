import os
import unittest
from shutil import rmtree
from utils import compare_file_tree


class BasicTest(unittest.TestCase):

    def test_rename_folder(self):
        os.system(
            "python3 ../rename_guru data/test_rename_folder/source "
            "data/test_rename_folder/output something else --perform"
        )
        compare_file_tree(
            "data/test_rename_folder/output",
            "data/test_rename_folder/match",
            lambda str1, str2: self.assertEqual(str1, str2)
        )

    def test_rename_nested_folder(self):
        os.system(
            "python3 ../rename_guru data/test_rename_nested_folder/source "
            "data/test_rename_nested_folder/output something else --perform"
        )
        compare_file_tree(
            "data/test_rename_nested_folder/output",
            "data/test_rename_nested_folder/match",
            lambda str1, str2: self.assertEqual(str1, str2)
        )

    def setUp(self):
        try:
            rmtree("data/%s/output" % self._testMethodName)
        except FileNotFoundError:
            pass
        os.mkdir("data/%s/output" % self._testMethodName)

    def tearDown(self):
        try:
            rmtree("data/%s/output" % self._testMethodName)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
