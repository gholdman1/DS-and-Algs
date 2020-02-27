"""Tests linkedlist.py"""

import pytest
import sys,os

# Add dsalgs package to path
filepath=os.path.abspath(__file__)
dsalgs_path=os.path.dirname(os.path.dirname(filepath))
sys.path.append(dsalgs_path)

from dsalgs.linkedlist import LinkedList

class TestLinkedList:

	def test_prepend(self):
		ll=LinkedList()
		ll.prepend(0)
		assert ll.head.x==0

	def test_append(self):
		ll=LinkedList()
		ll.append(0)
		assert ll.head.x==0