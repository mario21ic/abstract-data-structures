// FIFO: First in first in

class Queue {

  constructor() {
    this.items = [];
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    return this.items.shift();
  }

  peek() {
    return this.items[0];
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

const assert = require('assert').strict;

var cola = new Queue();
assert.strictEqual(true, cola.is_empty());

cola.enqueue(11);
cola.enqueue(22);
cola.enqueue(44);

assert.strictEqual(3, cola.size());

console.log(cola.items);

assert.strictEqual(11, cola.peek());

first_item = cola.dequeue();
assert.strictEqual(11, first_item);

console.log(cola.peek());

cola.dequeue();
console.log(cola.peek());
assert.strictEqual(44, cola.peek());

console.log(cola.size());
console.log(cola.is_empty());

cola.dequeue();
assert.strictEqual(true, cola.is_empty());

