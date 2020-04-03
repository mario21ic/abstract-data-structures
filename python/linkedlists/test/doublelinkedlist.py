#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from lib.DoubleLinkedList import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):

  def setUp(self):
    #self.sll = SingleLinkedList()
    pass

  def test_empty(self):
    dll = DoubleLinkedList()
    self.assertEqual(True, dll.empty())

  def test_not_empty(self):
    dll = DoubleLinkedList()
    dll.add(12)
    self.assertEqual(False, dll.empty())

  def test_get_link_values(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    items_expected = [12, 99, 37, 66]
    self.assertEqual(items_expected, dll.get_link_values())
    self.assertEqual(4, dll.count_links())

  def test_get_first(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    link = dll.get_first()
    self.assertEqual(12, link.value)

  def test_get_last(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    link = dll.get_last()
    self.assertEqual(37, link.value)

  def test_get_link(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    link = dll.get_link(99)
    self.assertEqual(99, link.value)
    self.assertEqual(37, link.next)
    self.assertEqual(12, link.prev)
    self.assertEqual(3, dll.count_links())

  def test_get_position(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    self.assertEqual(2, dll.get_position(37))

  def test_get_by_next(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    link = dll.get_by_next(37)
    self.assertEqual(99, link.value)
    self.assertEqual(37, link.next)
    self.assertEqual(12, link.prev)
    self.assertEqual(4, dll.count_links())

  def test_get_by_prev(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    link = dll.get_by_prev(99)
    self.assertEqual(37, link.value)
    self.assertEqual(66, link.next)
    self.assertEqual(99, link.prev)
    self.assertEqual(4, dll.count_links())

  def test_traverse(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    self.assertEqual([12, 99, 37], dll.traverse())
    self.assertEqual(3, dll.count_links())

  def test_traverse_from(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    dll.add(44)
    self.assertEqual([37, 66, 44], dll.traverse(37))
    self.assertEqual(5, dll.count_links())

  def test_traverse_back(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    self.assertEqual([37, 99, 12], dll.traverse_back())
    self.assertEqual(3, dll.count_links())

  def test_traverse_back_from(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    dll.add(44)
    self.assertEqual([66, 37, 99, 12], dll.traverse_back(66))
    self.assertEqual(5, dll.count_links())

  def test_delete(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    dll.add(44)
    dll.delete(37)
    self.assertEqual([12, 99], dll.traverse())
    self.assertEqual([66, 44], dll.traverse(66))
    self.assertEqual([99, 12], dll.traverse_back())
    self.assertEqual([44, 66], dll.traverse_back(44))
    self.assertEqual([12, 99, 66, 44], dll.get_link_values())
    self.assertEqual(4, dll.count_links())

  def test_delete_reconnect(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    dll.add(44)
    dll.delete(37, reconnect=True)
    self.assertEqual([12, 99, 66, 44], dll.traverse())
    self.assertEqual([44, 66, 99, 12], dll.traverse_back())
    self.assertEqual([12, 99, 66, 44], dll.get_link_values())
    self.assertEqual(4, dll.count_links())

  def test_update(self):
    dll = DoubleLinkedList()
    dll.add(12)
    dll.add(99)
    dll.add(37)
    dll.add(66)
    dll.update(99, 88)
    traverse_expected = [12, 88, 37, 66]
    self.assertEqual(traverse_expected, dll.traverse())
    traverse_expected.reverse()
    self.assertEqual(traverse_expected, dll.traverse_back())
    # items_expected = [12, 37, 66, 88]
    # self.assertEqual(items_expected, dll.get_link_values())
    self.assertEqual(4, dll.count_links())