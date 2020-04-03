// LIFO: Last in first in

class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    this.items.pop();
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  clear() {
    this.items = [];
  }

  size() {
    return this.items.length;
  }

  is_empty() {
    return this.size() == 0;
  }
}

var pila = new Stack();
pila.push(11);
pila.push(22);
pila.push(44);
console.log(pila.items);
console.log(pila.peek());
pila.pop();
console.log(pila.peek());
console.log(pila.size());
console.log(pila.is_empty());

const assert = require('assert').strict;
assert.strictEqual(false, pila.is_empty());

