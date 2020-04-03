# LIFO: last in first out

class Stack

  #attr_accessor :items
  #attr_writer :items
  attr_reader :items

  def initialize
    @items = []
  end

  def push(item)
    @items.push(item)
  end

  def pop
    @items.pop()
  end

  def top
    @items.last()
  end

  def is_empty
    @items.length() == 0
  end

  def size
    @items.length()
  end

  def clear
    @items = []
  end
end

