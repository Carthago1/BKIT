import unittest
from steps.qr import is_real
from steps.qr import get_roots

class TestQr(unittest.TestCase):

    def test1(self):
        self.assertTrue(len(get_roots(0, 0, 0)) > 4)
    def test2(self):
        self.assertEqual(get_roots(1, 1, 1), [])
    def test3(self):
        self.assertEqual(get_roots(-1, -1, -1), [])
    def test4(self):    
        self.assertEqual(get_roots(0, 0, 1), [])
    def test5(self):
        self.assertEqual(get_roots(9, 0, 0), [0, ])
    def test6(self):
        self.assertEqual(get_roots(0, 8, 0), [0, ])
    def test7(self):
        self.assertEqual(get_roots(31, 0, 87), [])
    def test8(self):
        self.assertEqual(get_roots(0, 1, 1), [])
    def test9(self):
        self.assertEqual(get_roots(10, 25, 0), [0, ])
    def test10(self):
        self.assertEqual(set(get_roots(10, -15, 0)), set([-6**0.5/2, 0, 6**0.5/2]))
    def test11(self):
        self.assertEqual(set(get_roots(0, 1, -16)), set([-4, 4]))
    def test12(self):
        self.assertEqual(set(get_roots(1, 0, -4)), set([-2**0.5, 2**0.5]))
    def test13(self):
        self.assertEqual(set(get_roots(1, -5, -36)), set([-3, 3]))
    def test14(self):
        self.assertEqual(set(get_roots(1, 14, 48)), set([]))
    def test15(self):
        self.assertEqual(set(get_roots(1, 1, -20)), set([-2, 2]))
    def test16(self):
        self.assertEqual(set(get_roots(1, -5, 4)), set([-2, -1, 1, 2]))
    def test17(self):
        self.assertEqual(set(get_roots(1, -5, 6)), set([-3**0.5, -2**0.5, 2**0.5, 3**0.5]))

    def test21(self):
        self.assertFalse(is_real('afaf'))
    def test22(self):
        self.assertFalse(is_real('213a'))
    def test23(self):
        self.assertFalse(is_real('23a21'))
    def test24(self):
        self.assertFalse(is_real('4.555555.1111'))
    def test25(self):
        self.assertFalse(is_real(',01234'))
    def test26(self):
        self.assertTrue(is_real('9873'))
    def test27(self):
        self.assertTrue(is_real('3.9123'))
    def test28(self):
        self.assertTrue(is_real(2345))
    def test29(self):
        self.assertTrue(is_real(5.5))
    def test30(self):
        self.assertFalse(is_real(complex(-5, 1)))
    

if __name__ == '__main__':
    unittest.main()
