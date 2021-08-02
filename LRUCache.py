# Maintain the doubly linkedlist and dictionary of node

class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key:int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertAtHead(node)
            return node.value
        
        return -1
    def put(self, key:int, value:int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            node.value = value
            self.insertAtHead(node)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = Node(key,value)
            self.insertAtHead(node)
            self.dic[key] = node
    
    def insertAtHead(self,node):
        head_next = self.head.next
        node.next = head_next
        node.prev = self.head
        self.head.next = node
        head_next.prev = node
    
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeFromTail(self, node):
        if len(self.dic) <= 0 :
            return
        before_tail = self.tail.prev
        del self.dic[before_tail.key]
        self.removeFromList(before_tail)
        
        
obj1 = LRUCache(5)
obj1.put(1,10)
obj1.put(2,2)
obj1.put(3,3)
param1 = obj1.get(1)
print(param1)