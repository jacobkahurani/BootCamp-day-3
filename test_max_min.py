import unittest
def find_max_min(li):
    most = li[0]
    least = li[0]
    for i in range(0,len(li)):
        if(li[i] > most):
            most = li[i]
    for i in range(0,len(li)):
        if(li[i] < least):
            least = li[i]
    if most == least or least == most:
        return [len(li)]
    else:
        return [least,most]
        
class MaxMinTest(unittest.TestCase):
    """docstring for MaxMinTest"""

    def test_find_max_min_four(self):
        self.assertEqual(find_max_min([1, 2, 3, 4]),[1, 4],msg='should return [1,4] for [1, 2, 3, 4]')

    def test_find_max_min_one(self):
        self.assertEqual(find_max_min([6, 4]),[4, 6],msg='should return [4, 6] for [6, 4]')

    def test_find_max_min_two(self):
        self.assertEqual(find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]),[2, 78],msg='should return [2, 78] for [4, 66, 6, 44, 7, 78, 8, 68, 2]')

    def test_find_max_min_three(self):
        self.assertEqual(find_max_min([1, 2, 3, 4]),[1, 4],msg='should return [1,4] for [1, 2, 3, 4]')

    def test_find_max_min_identity(self):
        self.assertEqual(find_max_min([4, 4, 4, 4]),[4],msg='Return the number of elements in the list in a new list if the `min` and `max` are equal')

if __name__ == '__main__':
    unittest.main()