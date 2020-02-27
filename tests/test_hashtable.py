"""Tests linkedlist.py"""

import pytest
import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.hashtable import HashTable

class TestHashTable:


	def test_get_size(self):
		ht = HashTable(10)

		assert ht.get_size()==10