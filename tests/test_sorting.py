"""Tests sorting.py"""

import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.sorting import mergesort

# Tests for any sorting algorithm

def sort_length_1(sort):

	arr = [1]
	arr = sort(arr)

	assert arr == [1]

def sort_negatives(sort):
	arr = [-5,-20,-34]
	arr = sort(arr)

	assert arr == [-34,-20,-5]

def sort_longer(sort):

	arr=[2,4,1,8,9,3,6,3,6,8,1,2,2,9,4,3,2,8]

	arr = sort(arr)

	assert arr == [1,1,2,2,2,2,3,3,3,4,4,6,6,8,8,8,9,9]

# Tests for mergesort
class TestMergeSort:

	def test_sort_length_1(self):
		sort_length_1(mergesort)

	def test_sort_negatives(self):
		sort_negatives(mergesort)

	def test_sort_longer(self):
		sort_negatives(mergesort)