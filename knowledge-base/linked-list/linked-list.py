class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 
        
class LinkedList:
    def __init__(self):
        self.head = None 
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head) # as for inserting in the first node, next node will be the existing self.head
        self.head = node
        
    def insert_at_end(self, data):
        node = Node(data, None) # as for the last node, next will be None
        
        if self.head is None:
            self.head = node 
            return 
        
        itr = self.head 
        
        while itr.next: 
            itr = itr.next 
            
        itr.next = node
        
    def insert_values(self, data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0 
        itr = self.head 
        
        while itr:
            count += 1
            itr = itr.next 
        
        return count 
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next 
            return 
        
        count = 0
        itr = self.head
        
        while itr:
            # need to stop in the node before the node to be removed 
            # as the next of that node will be the node to be removed
            if count == index - 1: 
                # as we are skipping the node to be removed
                # python will do the garbage collection
                itr.next = itr.next.next 
                break
            
            count += 1
            itr = itr.next 
            
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
            
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head 
        
        while itr: 
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node 
                break
            
            count += 1
            itr = itr.next
        
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr = self.head 
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next 
        
        print(llstr)

class DoublyNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def set_next(self, next):
        self.next = next 
        
    def set_prev(self, prev):
        self.prev = prev
    
    def get_data(self): 
        return self.data 
    
    def set_data(self, data):
        self.data = data
        
    def has_next(self):
        return self.get_next() is not None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get_size(self):
        return self.size
        
    def add(self, data):
        if self.size == 0:
            self.head = DoublyNode(data, None, None)
            self.tail = self.head
        else:
            node = DoublyNode(data, self.head)
            self.head.set_prev(node)
            self.head = node
        self.size += 1
        
        
    def remove(self, data):
        current_node = self.head
    
        while current_node is not None:
            if current_node.get_data() == data:
                if current_node.get_prev() is not None:
                    if current_node.has_next(): # delete middle node
                        current_node.get_prev().set_next(current_node.get_next())
                        current_node.get_next().set_prev(current_node.get_prev())
                    else: # delete last node
                        current_node.get_prev().set_next(None)
                        self.tail = current_node.get_prev()
                else: # delete first/head node
                    self.head = current_node.get_next()
                    current_node.get_next().set_prev(self.head)
                
                self.size -= 1
                return True
            else:
                current_node = current_node.get_next()
        return False
        
    def find(self, data):
        current_node = self.head 
        
        while current_node is not None:
            if current_node.get_data() == data:
                return data 
            elif current_node.get_next() == self.head:
                return None 
            else:
                current_node = current_node.get_next()
                
        return None
    
    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr = self.head 
        llstr = ''
        
        while itr.has_next():
            llstr += str(itr.data) + ' --> ' if itr.get_next() else str(itr.get_data())
            itr = itr.get_next() 
        
        print(llstr)
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    ll.print()
    print(ll.get_length())
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    print(ll.get_length())
    ll.insert_at(2, "pineapple")
    ll.print()
    print(ll.get_length())    
    ll.insert_at(0, "figs")
    ll.print()
    print(ll.get_length())
    
    doubleLinkedList = DoublyLinkedList()
    doubleLinkedList.add(5)
    doubleLinkedList.add(9)
    doubleLinkedList.add(3)
    doubleLinkedList.add(8)
    doubleLinkedList.add(9)
    print("size="+str(doubleLinkedList.get_size()))
    doubleLinkedList.print_list()
    doubleLinkedList.remove(8)
    doubleLinkedList.print_list()
    print("size="+str(doubleLinkedList.get_size()))
    print("Remove 15", doubleLinkedList.remove(15))
    doubleLinkedList.add(21)
    doubleLinkedList.add(22)
    doubleLinkedList.remove(5)
    doubleLinkedList.print_list()
    print("size="+str(doubleLinkedList.get_size()))
    print(doubleLinkedList.tail.get_prev())