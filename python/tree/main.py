from Arbol import Node, Tree


def main():
  """
  print("### Start: single nodes ###")
  root = Node("/")
  print(root)
  print(root.parent)

  child_left = Node("/boot", root)
  print(child_left)
  print(child_left.parent)

  child_right = Node("/var", root)
  print(child_right)
  print(child_right.parent)

  grandchild_right1 = Node("/run", child_right)
  print(grandchild_right1)
  print(grandchild_right1.parent)

  print("### End: single nodes ###")
  """

  tree = Tree()
  tree.insert("/")
  tree.insert("/root")
  tree.insert("/boot", "/")
  tree.insert("/etc", "/")
  tree.insert("/lib", "/")
  tree.insert("/var", "/")
  print("position_node /etc:", tree.position_node("/etc"))
  print("position_node /:", tree.position_node("/"))

  tree.insert("/hacker", "/home")
  tree.insert("/home", "/")
  tree.insert("/mario21ic", "/home")
  tree.insert("/steph", "/home")
  tree.insert("/Downloads", "/mario21ic")

  print("nodes:", tree.nodes)
  print("children's /:", tree.get_children("/"))
  print("children's /home:", tree.get_children("/home"))

  downloads_node = tree.get_node("/Downloads")
  print("downloads_node.label:", downloads_node)
  print("downloads_node.parent:", downloads_node.parent)
  print("full_path /Downloads:", tree.get_full_path("/Downloads"))

  tree.delete("/lib")
  print("deleted /lib, nodes:", tree.nodes)

  tree.insert("/Ares", "/Downloads")
  print("children's /steph:", tree.get_children("/steph"))
  tree.move_node("/Downloads", "/steph")
  print("children's /steph:", tree.get_children("/steph"))
  print("full_path /Ares:", tree.get_full_path("/Ares"))
  

if __name__=="__main__":
  main()
