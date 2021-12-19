import unittest
from functions import picture_path

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(picture_path('небольшой снег'),
         'D:\BKIT\dz\pictures\небольшой снег.png')
    def test2(self):
        self.assertEqual(picture_path('облачно с прояснениями'),
         'D:\BKIT\dz\pictures\облачно с прояснениями.png')

if __name__ == '__main__':
    unittest.main()