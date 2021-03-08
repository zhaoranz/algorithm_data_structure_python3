#first of all, define Nodes:
class Node(object):
    
    def __init__(self, val):
        
        self.val = val
        self.next = None
    
#define a single linked list:#
class SingleLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = Node(0)
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index+1):
            temp = temp.next
        return temp.val

    def is_empty(self):
        return self.head.next is None
    def addAtIndex(self,index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size +=1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = Node(val)
        to_add.next = pred.next
        pred.next = to_add
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
    def addAtHead(self, val):
        self.addAtIndex(0, val)
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

        
if __name__ =="__main__":
    ll = SingleLinkedList()
    #node1 = Node(1)
    #node2 = Node(2)
    ll.addAtHead(0)
    ll.addAtHead(1)
    
    ll.addAtHead(3)
    ll.addAtTail(5)
    ll.addAtTail(6)

    for i in range(ll.size):
        print(ll.get(i), ll.size)
        
