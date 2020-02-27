"""Tests linkedlist.py"""

import pytest
import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.hashtable import HashTable

class TestHashTableChaining:
	'''
	Tests a HashTable using collisionhandling=='chaining' option.
	'''

	@staticmethod
	def new_ht(slots):
		return HashTable(slots,collisionhandling='chaining')

	def test_get_size(self):
		ht = self.new_ht(10)

		assert ht.get_size()==10

class TestHashTableOpenAddressing:
	'''
	Tests a HashTable using collisionhandling=='openaddressing' option.
	'''

	@staticmethod
	def new_ht(slots):
		return HashTable(slots,collisionhandling='openaddressing')

	def test_get_size(self):
		ht = self.new_ht(10)

		assert ht.get_size()==10