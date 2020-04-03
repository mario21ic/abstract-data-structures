# LIFO: last in first out

class Stack:

  def __init__(self):
    self.items = []

  def clear(self):
    self.items = []

  def size(self):
    return len(self.items)

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def top(self):
    return self.items[-1]

  def is_empty(self):
    return self.size() == 0



