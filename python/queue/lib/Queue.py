# FIFO: first in, first out

class Queue:

  def __init__(self):
    self.items = []

  def clear(self):
    self.items = []

  def size(self):
    return len(self.items)

  def add(self, item):
    self.items.append(item)

  def remove(self):
    return self.items.pop(0)

  def front(self):
    return self.items[0]

  def is_empty(self):
    return self.size() == 0



