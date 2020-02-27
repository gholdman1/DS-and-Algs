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

	def test_insert(self):
		ht= self.new_ht(10)

		ht.insert(2)

		assert ht.table[2].head.x==2

	def test_get_keys(self):
		ht= self.new_ht(10)

		ht.insert(2)

		assert ht.get_keys()==1

	def test_get_keys_large_load_factor(self):
		ht=self.new_ht(5)

		for i in range(36):
			ht.insert(i)

		assert ht.get_keys() == 36

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