class Node:
  """
  Node in the Linked List
  """
  def __init__(self, key, data):
    self.key = key
    self.data = data
    self.prev = None
    self.next = None

  def __str__(self):
    return "[(%d, %s)]" % (self.key, self.data)

class DoublyList:
  """
  Implementation of dobuly linked list
  """
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, key, data):
    # create new Node
    node = Node(key, data)
    if (not self.head):
      self.head = node
      self.tail = node
    else:
      tail = self.tail
      tail.next = node
      node.prev = tail
      self.tail = node
 
  def move_to_front(self, node):
    if not self.head:
      self.head = node
      self.tail = node
    elif node == self.head:
      # do nothing
      pass
    elif node == self.tail:
      self.tail = self.tail.prev
      self.tail.next = None

      old_head = self.head
      self.head = node
      self.head.next = old_head
      old_head.prev = self.head

    else:
      # remove the node from the list
      node.prev.next = node.next
      node.next.prev = node.prev
      # make the node head of the list
      old_head = self.head
      self.head = node
      self.head.next = old_head
      old_head.prev = self.head

  def add_to_front(self, node):
    if not self.head:
      self.head = node
      self.tail = node
    else:
      old_head = self.head
      self.head = node
      self.head.next = old_head
      old_head.prev = self.head

  def remove_first(self):
    if not self.head:
      return None

    head = self.head
    self.head = head.next
    self.head.prev = None
    return head

  def remove_last(self):
    if not self.tail:
      return None

    tail = self.tail
    new_tail = tail.prev
    self.tail = new_tail
    if new_tail:
        new_tail.next = None
    else:
        # only one element
        self.head = None
    return tail

  def traverse(self, reverse = False):
    current = self.tail if reverse else self.head
    while (current):
      yield current
      current = current.prev if reverse else current.next

  def __str__(self):
    l = []
    print "Head = %s" % self.head
    print "Tail = %s" % self.tail
    current = self.head
    
    if not current:
      return "[]"

    while(current):
      l.append("%s" % (current, ))
      current = current.next
      
    return ' --> '.join(l)

class LRU:
  """
  Implementation of LRU cache which works in almost contant time
  LRU cache is implemented using python dictionary and Doubly Linked List 
  dictionary is used for look ups (i.e cache) and Doubly Linked List is used keeping track of recency of objects. 
  the objects which are used frequently are being kept near the head of the list and the ones which are not are kept towards the tail of the list

  Head of the List will always have most recetnly used object 
  Tail of the List will have least recently used object

  so whenever we need to purge any object from cache, we simply remove the one at the tail
  """
  def __init__(self, max_objects = 10):
    self.max = max_objects
    self.total = 0
    self.cache = {}
    self.list = DoublyList()

  def get(self, key):
    node = self.cache.get(key, None)
    if node: self.list.move_to_front(node)
    return node

  def put(self, key, data): 
    # check if already exist
    if key in self.cache:
      # just move this node to front of the list
      node = self.cache[key]
      node.data = data
      self.list.move_to_front(node)
    # key doesn't exist, and cache is full
    elif self.total == self.max:
      self._remove_oldest()
      node = Node(key, data)      
      self.list.add_to_front(node)
      self.total += 1
      self.cache[key] = node
    # key doesn't exist and cache is not full, then just add it and update the list
    else:
      node = Node(key, data)
      self.cache[key] = node
      self.list.add_to_front(node)
      self.total += 1

  def _remove_oldest(self):
    eldest = self.list.remove_last()
    # also remove this from the cache
    del self.cache[eldest.key]
    # decrement the count
    self.total -= 1

  def __str__(self):
    return "cache [%d] : %s \nreceny list :  %s" % (self.total, self.cache, self.list)

def main():
    n = 2
    cache = LRU(n)
    cache.put(2, 1)
    print "Cache : %s" % cache
    print "----------------------"
    cache.put(1, 1)
    print "Cache : %s" % cache
    print "----------------------"
    cache.put(2, 3)
    print "Cache : %s" % cache
    print "----------------------"
    cache.put(4, 1)
    print "Cache : %s" % cache
    print "----------------------"
    print "get(1)"
    print cache.get(1)
    print "Cache : %s" % cache
    print "----------------------"
    print "get(2)"
    print cache.get(2)
    print "Cache : %s" % cache
    print "----------------------"
    

if __name__ == "__main__":
  main()
