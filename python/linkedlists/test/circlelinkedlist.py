#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from lib.CircleLinkedList import CircleLinkedList


class TestCircleLinkedList(unittest.TestCase):

  def setUp(self):
    #self.sll = SingleLinkedList()
    pass

  def test_empty(self):
    cll = CircleLinkedList()
    self.assertEqual(True, cll.empty())

  def test_not_empty(self):
    cll = CircleLinkedList()
    cll.add(12)
    self.assertEqual(False, cll.empty())

  def test_circle_linked(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(24)
    cll.add(48)
    cll.add(96)

    link_first = cll.get_link(12)
    self.assertEqual(None, link_first.prev)
    self.assertEqual(24, link_first.next)
    self.assertEqual(None, link_first.start)
    self.assertEqual(96, link_first.end)

    link_middle = cll.get_link(24)
    self.assertEqual(12, link_middle.prev)
    self.assertEqual(48, link_middle.next)
    self.assertEqual(None, link_middle.start)
    self.assertEqual(None, link_middle.end)

    link_last = cll.get_link(48)
    self.assertEqual(24, link_last.prev)
    self.assertEqual(96, link_last.next)
    self.assertEqual(None, link_last.start)
    self.assertEqual(None, link_last.end)

    link_last = cll.get_link(96)
    self.assertEqual(48, link_last.prev)
    self.assertEqual(None, link_last.next)
    self.assertEqual(12, link_last.start)
    self.assertEqual(None, link_last.end)

    self.assertEqual(False, cll.empty())

  def test_get_link_values(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    items_expected = [12, 99, 37, 66]
    self.assertEqual(items_expected, cll.get_link_values())
    self.assertEqual(4, cll.count_links())

  def test_get_first(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    link = cll.get_first()
    self.assertEqual(12, link.value)

  def test_get_last(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    link = cll.get_last()
    self.assertEqual(37, link.value)

  def test_get_link(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    link = cll.get_link(99)
    self.assertEqual(99, link.value)
    self.assertEqual(37, link.next)
    self.assertEqual(12, link.prev)
    self.assertEqual(3, cll.count_links())

  def test_get_position(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    self.assertEqual(2, cll.get_position(37))

  def test_get_by_next(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    link = cll.get_by_next(37)
    self.assertEqual(99, link.value)
    self.assertEqual(37, link.next)
    self.assertEqual(12, link.prev)
    self.assertEqual(4, cll.count_links())

  def test_get_by_prev(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    link = cll.get_by_prev(99)
    self.assertEqual(37, link.value)
    self.assertEqual(66, link.next)
    self.assertEqual(99, link.prev)
    self.assertEqual(4, cll.count_links())

  def test_traverse(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    self.assertEqual([12, 99, 37], cll.traverse())
    self.assertEqual(3, cll.count_links())

  def test_traverse_from(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    cll.add(44)
    self.assertEqual([37, 66, 44], cll.traverse(37))
    self.assertEqual(5, cll.count_links())

  def test_traverse_back(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    self.assertEqual([37, 99, 12], cll.traverse_back())
    self.assertEqual(3, cll.count_links())

  def test_traverse_back_from(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    cll.add(44)
    self.assertEqual([66, 37, 99, 12], cll.traverse_back(66))
    self.assertEqual(5, cll.count_links())

  def test_delete(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    cll.add(44)
    cll.delete(37)
    self.assertEqual([12, 99], cll.traverse())
    self.assertEqual([66, 44], cll.traverse(66))
    self.assertEqual([99, 12], cll.traverse_back())
    self.assertEqual([44, 66], cll.traverse_back(44))
    self.assertEqual([12, 99, 66, 44], cll.get_link_values())
    self.assertEqual(4, cll.count_links())

  def test_delete_reconnect(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    cll.add(44)
    cll.delete(37, reconnect=True)
    self.assertEqual([12, 99, 66, 44], cll.traverse())
    self.assertEqual([44, 66, 99, 12], cll.traverse_back())
    self.assertEqual([12, 99, 66, 44], cll.get_link_values())
    self.assertEqual(4, cll.count_links())

  def test_update(self):
    cll = CircleLinkedList()
    cll.add(12)
    cll.add(99)
    cll.add(37)
    cll.add(66)
    cll.update(99, 88)
    traverse_expected = [12, 88, 37, 66]
    self.assertEqual(traverse_expected, cll.traverse())
    traverse_expected.reverse()
    self.assertEqual(traverse_expected, cll.traverse_back())
    # items_expected = [12, 37, 66, 88]
    # self.assertEqual(items_expected, cll.get_link_values())
    self.assertEqual(4, cll.count_links())