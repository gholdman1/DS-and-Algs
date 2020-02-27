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
		pass
