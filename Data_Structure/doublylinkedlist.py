class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True # to use append in insert method
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
        """ More readable -> 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
        """

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            self.head.prev = new_node
            new_node.next = self.head # order?
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next

        after.prev = temp.prev
        before.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
dllist = DoublyLinkedList(1)
dllist.print_list()
print()

dllist.append(2)
dllist.append(3)
dllist.print_list()
print()

dllist.pop()
dllist.prepend(0)
dllist.print_list()
print()

dllist.pop_first()
dllist.print_list()
print()

dllist.get(1)
dllist.set_value(1,10)
dllist.print_list()
print()

dllist.insert(1,5)
dllist.insert(3,5)
dllist.insert(0,6)
dllist.print_list()
print()

dllist.remove(1)
dllist.remove(3)
dllist.remove(0)
dllist.remove(1)
dllist.remove(3)
dllist.print_list()
print()