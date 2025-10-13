class Node():
    def __init__(self, Value):
        self.value = Value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def isEmpty(self):
        return self.head is None
        
    def find(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        raise IndexError("Index out of bounds")

    def delete(self, index):
        if self.isEmpty():
            raise IndexError("Can't delete from empty list")
        if index < 0 or index >= self.size:
            raise IndexError("Deletion index out of bounds")

        
        if index == 0:
            removed = self.head.value
            self.head = self.head.next
            
            if self.head is None:
                self.tail = None
            self.size -= 1
            return removed

        current = self.head
        for _ in range(index - 1):
            current = current.next

        removed_value = current.next.value
        current.next = current.next.next

        if current.next is None:
            self.tail = current
        self.size -= 1
        return removed_value

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Insert out of bounds, Size:", self.size)
        
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if self.size == 0:
                self.tail = new_node
            self.size += 1
            return new_node

        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
            return new_node
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return new_node
        
    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return f"{values}"
    

    def __len__(self):
        return self.size

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        
        if self._iter_node:
            value = self._iter_node.value
            self._iter_node = self._iter_node.next
            return value
        
        raise StopIteration




class Stack:
    def __init__(self):
        self.data = LinkedList()
    
    def push(self, Value):
        self.data.insert(0, Value)

    def pop(self):
        if not self.data.isEmpty():
            self.data.delete(0)
        else:
            raise IndexError("Cannot pop an empty stack.")

    def peek(self):
        if not self.data.isEmpty():
            return self.data.find(0)
        else:
            raise IndexError("Cannot peek at an empty stack.")

    def __str__(self):
        return f"{self.data.__str__()}"
    
class Queue:
    def __init__(self):
        self.data = LinkedList()
    
    def pushEnd(self, value):
        self.data.add(value)
    
    def pushFirst(self, value):
        self.data.insert(0, value)

    def popEnd(self):
        if not self.data.isEmpty():
            self.data.delete(self.data.size-1)
        else:
            raise IndexError("Cannot pop an empty queue.")
    
    def popFirst(self):
        if not self.data.isEmpty():
            self.data.delete(0)
        else:
            raise IndexError("Cannot pop an empty queue.")
    def __str__(self):
        return f"{self.data.__str__()}"

class PriorityValue:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.data = LinkedList()
    
    def push(self, value, priority):
        self.data.add(PriorityValue(value, priority))
    
    def pop(self):
        if self.data.isEmpty():
            raise IndexError("can't pop from empty queue")
        index = 0
        i = 0
        maxpriority = float("-inf")
        for value in self.data:
            if value.priority > maxpriority:
                maxpriority = value.priority
                index = i
            i += 1
        self.data.delete(index)

    def __str__(self):
        Printables = []
        for PriorityValue in self.data:
            Printables.append(PriorityValue.value)
        return f'{Printables}'
