def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i
        left_sum += num
    return -1

print(equilibrium_index([1,2,3,4,3,2,1]))


import unittest

class TestEquilibriumIndex(unittest.TestCase):

#Test Case 1
    def test_equilibrium_index_1(self):
        self.assertEqual(equilibrium_index([1,2,3,4,3,2,1]), 3)

#Test Case 2
    def test_equilibrium_index_2(self):
        self.assertEqual(equilibrium_index([1,2,3,4,5,6,7]), -1)

#Test Case 3
    def test_equilibrium_index_3(self):
        self.assertEqual(equilibrium_index([1,2,3,4,5,6,5,4,3,2,1]), 6)

#Test Case 4
    def test_equilibrium_index_4(self):
        self.assertEqual(equilibrium_index([1,0,1]), 1)

#Test Case 5
    def test_equilibrium_index_5(self):
        self.assertEqual(equilibrium_index([3,3,3]), -1)
