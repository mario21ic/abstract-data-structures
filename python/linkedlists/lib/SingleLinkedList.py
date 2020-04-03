# TODO: teoria de conjuntos con listas, eliminar duplicados, encontrar huerfanos

class Node:

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

  #def __repr__(self):
  #  return str(self.value)


class SingleLinkedList:

  def __init__(self):
    self.links = []

  def empty(self):
    return (len(self.links) == 0)

  def count_links(self):
    return len(self.links)

  def get_by_next(self, next_value):
    link_return = None
    for link in self.links:
      if link.next == next_value:
        link_return = link
        break
    return link_return

  def get_link_values(self):
    values = []
    for link in self.links:
      values.append(link.value)
    return values

  def get_link(self, value):
    for link in self.links:
      if link.value == value:
        return link
    return None

  def get_first(self):
    return self.links[0]

  def get_last(self):
    for link in self.links:
      if link.next is None:
        return link
    return None

  def update(self, value, new_value):
    link_old = self.get_link(value)
    link_new = Node(new_value)
    link_new.next = link_old.next

    link_next = self.get_by_next(value)
    self.links.append(link_new)

    self.delete(value)
    link_next.next = link_new.value

  def add(self, value):
    link_last = self.get_last()
    link_new = Node(value)
    if link_last is not None:
      link_last.next = link_new.value
    self.links.append(link_new)

  def delete(self, value, reconnect=False):
    position = self.get_position(value)
    next_value = None
    if reconnect:
      link_tmp = self.get_link(value)
      next_value = link_tmp.next

    del self.links[position]
    link_next = self.get_by_next(value)
    link_next.next = next_value

  def get_position(self, value):
    x = 0
    while x < len(self.links):
      if value == self.links[x].value:
        position = x
        break
      x += 1
    return position

  def traverse(self, value=None):
    values = []
    if value is None:
      node = self.get_first()
    else:
      node = self.get_link(value)

    while node is not None:
      values.append(node.value)
      node = self.get_link(node.next)

    return values

