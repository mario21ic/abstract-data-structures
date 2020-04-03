require "./stack"

require 'test/unit'


class StackTest < Test::Unit::TestCase

  def test_empty
    stack = Stack.new
    assert_equal true, stack.is_empty
  end

  def test_lifo
    stack = Stack.new()
    stack.push(11)
    stack.push(22)
    stack.push(44)
    assert_equal(44, stack.top())

    stack.pop()
    assert_equal(22, stack.top())
    assert_equal(2, stack.size())
    assert_equal(false, stack.is_empty())

    stack.pop()
    assert_equal(11, stack.top())

    stack.pop()
    assert_equal(true, stack.is_empty())
  end

  def test_clear
    stack = Stack.new
    stack.push(11)
    stack.push(22)
    stack.clear()
    assert_equal true, stack.is_empty
  end

end
