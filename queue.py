class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def enqueue(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
    if self.tail:
      self.tail.next = node
    self.tail = node

    self.size += 1

  def dequeue(self):
    if self.head is None:
      return None

    value = self.head.value
    if self.head is self.tail:
      self.tail = None

    self.head = self.head.next
    self.size -= 1
    return value

  def isNotEmpty(self):
    return self.size > 0

  def __repr__(self):
    node = self.head
    s = ""
    while node:
      s += str(node.value) + ' -> '
      node = node.next
    return s


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

array = [3,4,5,6,7,8,9]

q = Queue()

for n in array:
  q.enqueue(n)

print(q)
while q.isNotEmpty():
  print(q.dequeue())
print(q)

