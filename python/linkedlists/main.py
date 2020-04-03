#from LinkedList import Node, DoubleNode
from lib.SingleLinkedList import SingleLinkedList
from lib.DoubleLinkedList import DoubleLinkedList


def main():
  """
  print("### Node")
  node1 = Node(12)
  node2 = Node(99)
  node3 = Node(37)
  node4 = Node(66)

  node1.next = node2
  node2.next = node3
  node3.next = node4

  node1.traverse()

  print("### DoubleNode")
  dnode1 = DoubleNode(12)
  dnode2 = DoubleNode(99)
  dnode3 = DoubleNode(37)

  dnode1.next = dnode2
  dnode2.prev = dnode1
  dnode2.next = dnode3
  dnode3.prev = dnode2

  dnode1.traverse()
  dnode3.traverse_back()
  """

  """
  #items = [12, 99, 37, 66]
  #sll = SingleLinkedList(items)
  sll = SingleLinkedList()
  sll.add(12)
  sll.add(99)
  sll.add(37)
  sll.add(66)
  sll.traverse()
  sll.add(44)

  link66 = sll.get_link(66)
  print("link66: value=%s next=%s" % (link66.value, link66.next))
  print("links: %s" % (sll.links))
  link_last = sll.get_last()
  print("link_last: value=%s next=%s" % (link_last.value, link_last.next))

  sll.traverse(37)
  print("get_position 99")
  print(sll.get_position(99))

  #link37 = sll.get_by_next(37)
  #print("link37:", link37.value)

  print("update 99 - 88")
  sll.update(99, 88)
  print("links: %s" % (sll.links))
  sll.traverse()

  print("delete 66")
  sll.delete(66)
  print("links: %s" % (sll.links))
  sll.traverse()
  """

  dll = DoubleLinkedList()
  dll.add(12)
  dll.add(99)
  dll.add(37)
  dll.add(66)
  dll.add(44)
  print("links: %s" % (dll.links))
  dll.traverse()
  dll.traverse(99)

  dll.traverse_back()
  dll.traverse_back(37)

  link_by66 = dll.get_link(66)
  print("link_by66: value=%s next=%s prev=%s" % (link_by66.value, link_by66.next, link_by66.prev))
  link_next66 = dll.get_by_next(66)
  print("link_next66: value=%s next=%s prev=%s" % (link_next66.value, link_next66.next, link_next66.prev))
  link_prev66 = dll.get_by_prev(66)
  print("link_prev66: value=%s next=%s prev=%s" % (link_prev66.value, link_prev66.next, link_prev66.prev))

if __name__=="__main__":
  main()
