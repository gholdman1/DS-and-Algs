"""Tests sorting.py"""

import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.sorting import mergesort

class SortingTester:

	def __init__(self,sort):
		self.sort=sort

	def test_sort_length_1(self):

		arr = [1]
		arr = self.sort(arr)

		assert arr == [1]

	def test_sort_negatives(self):

		arr = [-5,-20,-34]
		arr = self.sort(arr)

		assert arr == [-34,-20,-5]

	def test_sort_longer(self):

		arr=[2,4,1,8,9,3,6,3,6,8,1,2,2,9,4,3,2,8]

		arr = self.sort(arr)

		assert arr == [1,1,2,2,2,2,3,3,3,4,4,6,6,8,8,8,9,9]