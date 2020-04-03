from lib.Stack import Stack

def main():
  pila = Stack()
  pila.insert(12)
  pila.insert(24)
  pila.insert(48)
  pila.insert(96)

  print(pila.items)
  print(pila.inspect())

  pila.next()
  print(pila.items)
  print(pila.is_empty())

  pila.clear()
  print(pila.is_empty())
  print("items", pila.items)


if __name__=="__main__":
  main()

