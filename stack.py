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
