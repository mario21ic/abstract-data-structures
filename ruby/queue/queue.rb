# FIFO: first in first out

class Queue

  #attr_accessor :items
  #attr_writer :items
  attr_reader :items

  def initialize
    @items = []
  end

  def add(item)
    @items.push(item)
  end

  def remove
    @items.shift()
  end

  def front
    @items.first()
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

