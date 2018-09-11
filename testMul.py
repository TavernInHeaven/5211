from RecurMulti import task1
import unittest
class Test2PositiveIntMultiply(unittest.TestCase):

    def testPosMulPos(self):
        self.assertEqual(task1(3, 7), 21)

    def testPosMulNeg(self):
        self.assertEqual(task1(7, -7), -49)

    def testPosMulZero(self):
        self.assertEqual(task1(6, 0), 0)

    def testZeroMulPos(self):
        self.assertEqual(task1(0, 3), 0)

    def testZeroMulNeg(self):
        self.assertEqual(task1(0, -8), 0)

    def testNegMulPos(self):
        self.assertEqual(task1(-5, 3), -15, "-5 * 3 = -15")

    def testNegMulZero(self):
        self.assertEqual(task1(-7,0), 0, "-7 * 0 = 0")

    def testNegMulNeg(self):
        self.assertEqual(task1(-9,-9), 81)
