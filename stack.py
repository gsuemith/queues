class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
  
  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node
    self.size += 1

  def peak(self):
    if self.top is None:
      return None

    return self.top.value

  def pop(self):
    node = self.top
    if self.top:
      self.top = self.top.next

    self.size -= 1
    return node.value

  def isEmpty(self):
    return self.size == 0

  def isNotEmpty(self):
    return self.size > 0

a = [1,2,3,4,5,6]

stk = Stack()

for n in a:
  stk.push(n)

while stk.isNotEmpty():
  print(stk.pop(), stk.peak())
