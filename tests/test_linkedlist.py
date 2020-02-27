"""Tests linkedlist.py"""

import pytest
import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.linkedlist import LinkedList

class TestLinkedList:

	def __init__(self):
		self.test_ds=LinkedList()

	def test_insert(self):
		pass
