import unittest
from HW01_Gengwu_Zhao import classify_triangle
class test_list_copy(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertTrue(classify_triangle(1,1,1)=='equilateral')
        self.assertTrue(classify_triangle(1,2,2)=='isosceles')
        self.assertTrue(classify_triangle(2,1,2)=='isosceles')
        self.assertTrue(classify_triangle(3,4,5)=='right')
        self.assertTrue(classify_triangle(4,2,3)=='scalene')
        with self.assertRaises(ValueError):
            classify_triangle(1,2,3)
        with self.assertRaises(ValueError):
            classify_triangle(1,0,0)
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)