"""Tests sorting.py"""

import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.searching import binarysearch

class TestBinarySearch:

	def test_empty(self):
		'''
		No key should be found in an empty array
		'''
		arr=[]

		assert binarysearch(arr,1,0,len(arr)-1) == -1

	def test_single_exists(self):
		'''
		Should find a single key in an array
		'''
		arr=[1]

		assert binarysearch(arr,1,0,len(arr)-1) == 0

	def test_single_not_exists(self):
		'''
		Should not find a key in a len==1 array if it does not exist.
		'''
		arr=[2]

		assert binarysearch(arr,1,0,len(arr)-1) == -1

	def test_many_exists(self):
		'''
		Should find a key in a small array
		'''
		arr=[1,2,5,6,7,10,20,22,24,26,26,28]

		assert binarysearch(arr,20,0,len(arr)-1) == 6

	def test_first_returned(self):
		'''
		Returns the first index if many keys are found.
		'''
		arr=[1,2,3,4,4,4,4,4,6]

		assert binarysearch(arr,4,0,len(arr)-1) == 3

	def test_finds_at_end(self):
		'''
		Finds a key at the end of an array
		'''
		arr=[1,2,5,7,9,10]

		assert binarysearch(arr,10,0,len(arr)-1) == 5

	def test_many_not_exists(self):
		'''
		Shows there is no key if it doesn't exist
		'''

		arr=[1,2,3,5,7,8,10,13,15,16,17,20,22,24,25]

		assert binarysearch(arr,4,0,len(arr)-1) == -1