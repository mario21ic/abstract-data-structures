require "./queue"

cola = Queue.new
cola.push(11)
cola.push(22)
cola.push(44)

puts "Items: #{cola.items}"
puts "Empty? #{cola.is_empty()}"
puts "Top #{cola.top()}"

cola.pop()
puts "Top #{cola.top()}"
cola.pop()
puts "Top #{cola.top()}"

cola.pop()
puts "Empty? #{cola.is_empty()}"
