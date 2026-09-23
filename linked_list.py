class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Write a function, find_largest, that takes in the head of a linked list containing numbers as an argument. The function should return the largest value found of in the linked list.

def find_largest(head, largest):

  if head is None:
    if largest == float("-inf"):
      return None
    return largest
  if head.val > largest:
    return find_largest(head.next, head.val)
  return find_largest(head.next, largest)


a = Node(1)
b = Node(4)
c = Node(8)
d = Node(8)
e = Node(3)
f = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print(find_largest(a, float("-inf")))

# sum linked list while vs recursion
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  current = head
  sum = 0
  while current is not None:
    sum += current.val
    current = current.next
  return sum
  
def sum_list(head):
  if head is None:
    return 0
  else:
    return head.val + sum_list(head.next)
