class Node:

  def __init__(self, label, parent=None):
    self.label = label
    self.parent = parent

  def __str__(self):
    return self.label

  def __repr__(self):
    return self.label

  def have_parent(self):
    return self.parent == None


class Tree:
  
  def __init__(self):
    self.root = None
    self.nodes = []

  #def __str__(self):
  #  return self.root.__str__()

  def position_node(self, label):
    #print("nodes:", self.nodes)
    position = 0
    for node in self.nodes:
      #print("node:", node.label)
      if node.label == label:
        return position
      position += 1
    return position

  def exists_node(self, label):
    #print("nodes:", self.nodes)
    for node in self.nodes:
      #print("node:", node.label)
      if node.label == label:
        return True
    return False

  def get_children(self, parent):
    children = []
    for node in self.nodes:
      #print("node,parent:", node.parent)
      if node.parent == parent:
        children.append(node)
    return children

  def get_node(self, label):
    node_return = None
    for node in self.nodes:
      #print("node.label:", node.label)
      if node.label == label:
        node_return = node
    return node_return

  def get_full_path(self, label):
    full_path = []
    node_obj = self.get_node(label)
    full_path.append(node_obj.label)
    #print("node_obj.parent:", node_obj.parent)
    is_done = False
    while is_done == False:
      for node in self.nodes:
        #print("node.label:", node.label)
        #print("node.parent:", node.parent)
        #print("node_obj.parent:", node_obj.parent)
        if node.label == node_obj.parent:
          full_path.append(node.label)
          node_obj = self.get_node(node.label)
          #print("new node_obj:", node_obj)
          if node.label == self.root:
            is_done = True
    full_path.reverse()
    return "".join(full_path)

  def insert(self, label, parent=None):
    node_new = Node(label, parent)
    if parent == None and self.root is None:
      self.root = label
      self.nodes.append(node_new)
      return True
    else:
      #print(self.exists_node(parent))
      if self.exists_node(parent):
        self.nodes.append(node_new)
        return True
    print("No es posible agregar %s en %s" % (label, parent))
    return False

  def move_node(self, label, new_parent):
    if self.exists_node(label):
      node = self.get_node(label)
      print("node.parent:", node.parent)
      node.parent = new_parent
      return True
    return False

  def delete(self, label):
    #print(self.exists_node(parent))
    if self.exists_node(label):
      del self.nodes[self.position_node(label)]
      return True
    return False

  def empty(self):
    if len(self.nodes) == 0:
      return True
    return False

