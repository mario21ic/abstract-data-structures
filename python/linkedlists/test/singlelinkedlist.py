#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from lib.SingleLinkedList import SingleLinkedList


class TestSingleLinkedList(unittest.TestCase):

  def setUp(self):
    #self.sll = SingleLinkedList()
    pass

  def test_empty(self):
    sll = SingleLinkedList()
    self.assertEqual(True, sll.empty())

  def test_not_empty(self):
    sll = SingleLinkedList()
    sll.add(12)
    self.assertEqual(False, sll.empty())
    self.assertEqual(1, sll.count_links())

  def test_get_link_values(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    sll.add(66)
    items_expected = [12, 99, 37, 66]
    self.assertEqual(items_expected, sll.get_link_values())
    self.assertEqual(4, sll.count_links())

  def test_get_first(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    link = sll.get_first()
    self.assertEqual(12, link.value)
    self.assertEqual(99, link.next)

  def test_get_last(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    link = sll.get_last()
    self.assertEqual(37, link.value)
    self.assertEqual(None, link.next)

  def test_get_link(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    link = sll.get_link(99)
    self.assertEqual(99, link.value)
    self.assertEqual(37, link.next)

  def test_get_position(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    self.assertEqual(2, sll.get_position(37))

  def test_get_by_next(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    sll.add(66)
    link = sll.get_by_next(37)
    self.assertEqual(99, link.value)

  def test_traverse(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    self.assertEqual([12, 99, 37], sll.traverse())
    self.assertEqual(3, sll.count_links())

  def test_traverse_from(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    sll.add(66)
    sll.add(44)
    self.assertEqual([37, 66, 44], sll.traverse(37))
    self.assertEqual(5, sll.count_links())

  def test_delete(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    sll.add(66)
    sll.add(44)
    sll.delete(37)
    self.assertEqual([12, 99], sll.traverse())
    self.assertEqual([12, 99, 66, 44], sll.get_link_values())
    self.assertEqual(4, sll.count_links())

  def test_delete_reconnect(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    sll.add(66)
    sll.add(44)
    sll.delete(37, reconnect=True)
    self.assertEqual([12, 99, 66, 44], sll.traverse())
    self.assertEqual([12, 99, 66, 44], sll.get_link_values())
    self.assertEqual(4, sll.count_links())

  def test_update(self):
    sll = SingleLinkedList()
    sll.add(12)
    sll.add(99)
    sll.add(37)
    sll.add(66)
    sll.update(99, 88)
    self.assertEqual([12, 88, 37, 66], sll.traverse())
    self.assertEqual(4, sll.count_links())


if __name__ == '__main__':
    unittest.main()

