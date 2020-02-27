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

	def test_insert_after(self):
		'''
		Tests insert_after method by creating LinkedList of length 1 and inserting after head.
		'''
		ll=LinkedList()
		ll.prepend(0)
		ll.insert_after(1,ll.head)
		assert ll.head.next.x == 1

	def test_delete_unique_value(self):
		'''
		Tests delete method when value is unique.
		'''

		ll=LinkedList()

		ll.prepend(0)
		ll.append(1)

		assert ll.head.next.x == 1

		ll.delete(1)

		assert ll.head.next == None

	def test_delete_first_of_two(self):
		'''
		Tests delete method when two equal values occur in list.
		Only first occurrence of value ought to be deleted.
		'''

		ll=LinkedList()

		ll.prepend(0)
		ll.append(1)
		ll.append(2)
		ll.append(0)

		ll.delete(0)

		assert ll.head.x==1
		assert ll.head.next.next.x==0