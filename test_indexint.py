from unittest import TestCase
from indexint import searchMiddle
from indexint import example

class TestIndexint(TestCase):
    def testCase(self):
        self.assertEqual(example([1,2,3]),True)

    def testNotExistReturnFalse(self):
        self.assertEqual(example([4,5,6]),False)

    def testDuplicatedItemShouldNotProceed(self):
        self.assertEqual(example([3,3,1]),False)
