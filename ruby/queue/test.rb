require "./queue"

require 'test/unit'


class QueueTest < Test::Unit::TestCase

  def test_empty
    queue = Queue.new
    assert_equal true, queue.is_empty
  end

  def test_fifo
    queue = Queue.new()
    queue.add(44)
    queue.add(22)
    queue.add(11)
    assert_equal(44, queue.front())

    queue.remove()
    assert_equal(22, queue.front())
    assert_equal(2, queue.size())
    assert_equal(false, queue.is_empty())

    queue.remove()
    assert_equal(11, queue.front())

    queue.remove()
    assert_equal(true, queue.is_empty())
  end

  def test_clear
    queue = Queue.new
    queue.add(11)
    queue.add(22)
    queue.clear()
    assert_equal true, queue.is_empty
  end

end
