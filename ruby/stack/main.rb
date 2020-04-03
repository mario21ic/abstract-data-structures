require "./stack"

pila = Stack.new
pila.push(11)
pila.push(22)
pila.push(44)

puts "Items: #{pila.items}"
puts "Empty? #{pila.is_empty()}"
puts "Top #{pila.top()}"

pila.pop()
puts "Top #{pila.top()}"
pila.pop()
puts "Top #{pila.top()}"

pila.pop()
puts "Empty? #{pila.is_empty()}"
