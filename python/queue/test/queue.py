#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from lib.Queue import Queue


class TestQueue(unittest.TestCase):

  def setUp(self):
    pass

  def test_empty(self):
    queue = Queue()
    self.assertEqual(True, queue.is_empty())

  def test_fifo(self):
    queue = Queue()
    queue.add(11)
    queue.add(22)
    queue.add(44)
    self.assertEqual(11, queue.front())

    last = queue.remove()
    self.assertEqual(11, last)
    self.assertEqual(22, queue.front())

    queue.remove()
    self.assertEqual(44, queue.front())

    queue.remove()
    self.assertEqual(True, queue.is_empty())

  def test_clear(self):
    queue = Queue()
    queue.add(11)
    queue.add(22)
    queue.clear()
    self.assertEqual(True, queue.is_empty())


