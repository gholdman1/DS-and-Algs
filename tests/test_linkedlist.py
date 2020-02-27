"""Tests linkedlist.py"""

import pytest
import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.linkedlist import LinkedList

class TestLinkedList:

	def test_empty_prepend(self):
		'''
		Tests prepend method on an empty LinkedList.
		'''
		ll=LinkedList()
		ll.prepend(0)
		assert ll.head.x==0

	def test_empty_append(self):
		'''
		Tests append method on an empty LinkedList.
		'''
		ll=LinkedList()
		ll.append(0)
		assert ll.head.x==0