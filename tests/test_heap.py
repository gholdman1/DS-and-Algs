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

		assert h.get_size() == 10

	def test_parent(self):
		'''
		Tests that parent index is correct.
		'''

		h = Heap(10)

		assert h.parent(2) == 0
		assert h.parent(1) == 0

	def test_insert(self):
		h=Heap(10)

		for i in range(10):
			h.insert(i)

	def test_get_keys(self):

		h = Heap(10)

		assert h.get_keys()==0

		h.insert(0)

		assert h.get_keys()==1

	def test_height(self):
		'''
		Test height of Heap as filled
		'''
		h = Heap(10)

		assert h.height() == 0

		h.insert(0)

		assert h.height() == 1