from lib.Queue import Queue

def main():
  cola = Queue()
  cola.insert(12)
  cola.insert(24)
  cola.insert(48)
  cola.insert(96)

  print(cola.items)
  print(cola.inspect())

  cola.next()
  print(cola.items)
  print(cola.is_empty())

  cola.clear()
  print(cola.is_empty())
  print("items", cola.items)


if __name__=="__main__":
  main()

