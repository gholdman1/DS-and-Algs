"""Tests linkedlist.py"""

import pytest
import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.heap import Heap

class TestHeap:
	'''
	Tests a HashTable using collisionhandling=='chaining' option.
	'''

	def test_get_size(self):
		h = Heap(10)

		assert h.get_size() == 16

	def test_parent(self):
		'''
		Tests that parent index is correct.
		'''

		h = Heap(16)

		assert h.parent(2) == 0
		assert h.parent(1) == 0

	def test_level(self):
		'''
		Test level method.
		'''

		h = Heap(16)

		assert h.level(0) == 0
		assert h.level(2) == 1
		assert h.level(3) == 2
		assert h.level(6) == 2
		assert h.level(7) == 3


	def test_insert(self):
		h=Heap(16)

		for i in range(16):
			h.insert(i)

	def test_get_keys(self):

		h = Heap(16)

		assert h.get_keys()==0

		h.insert(0)

		assert h.get_keys()==1

	def test_height(self):
		'''
		Test height of Heap as filled
		'''
		h = Heap(16)

		assert h.height() == 0

		h.insert(0)

		assert h.height() == 1

	def test_make_arr(self):
		'''
		Tests make arr
		'''

		arr = [4,6,7,8,1]

		h = Heap(16)
		h.make_heap(arr)

		assert h.arr[0]==1
		assert h.arr[0] < h.arr[1]
		assert h.arr[0] < h.arr[2]

	def test_insert(self):
		'''
		Tests insert method.
		'''

		arr = [4,6,1]

		h = Heap(10)
		h.make_heap(arr)

		h.insert(7)

		assert h.arr[3] == 7
		assert h.arr[0] == 1

