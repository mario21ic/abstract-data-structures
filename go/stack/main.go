package main

import (
  "fmt"
)

type Node struct {
  Value int
}

func (n *Node) String() string {
  return fmt.Sprint(n.Value)
}

func NewStack() *Stack {
  return &Stack{}
}

type Stack struct {
  nodes []*Node
  count int
}

func (s *Stack) Push(n *Node) {
  s.nodes = append(s.nodes[:s.count], n)
  s.count++
}

func (s *Stack) Pop() *Node {
  if s.count == 0 {
    return nil
  }
  s.count--
  return s.nodes[s.count]
}

func main() {
  s := NewStack()
  s.Push(&Node{1})
  s.Push(&Node{2})
  s.Push(&Node{3})
  fmt.Println(s.Pop())
  fmt.Println(s.Pop(), s.Pop())
}
