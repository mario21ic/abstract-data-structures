#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from lib.Stack import Stack


class TestStack(unittest.TestCase):

  def setUp(self):
    pass

  def test_empty(self):
    stack = Stack()
    self.assertEqual(True, stack.is_empty())

  def test_lifo(self):
    stack = Stack()
    stack.push(11)
    stack.push(22)
    stack.push(44)
    self.assertEqual(44, stack.top())

    stack.pop()
    self.assertEqual(22, stack.top())
    self.assertEqual(2, stack.size())
    self.assertEqual(False, stack.is_empty())

    stack.pop()
    self.assertEqual(11, stack.top())

    stack.pop()
    self.assertEqual(True, stack.is_empty())

  def test_clear(self):
    stack = Stack()
    stack.push(11)
    stack.push(22)
    stack.clear()
    self.assertEqual(True, stack.is_empty())
