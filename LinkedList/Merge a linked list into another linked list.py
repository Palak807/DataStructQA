class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        if self.length == 0:
            return None
        LL1 = LinkedList(0)
        LL1.make_empty()
        LL2 = LinkedList(0)
        LL2.make_empty()
        temp = self.head
        for _ in range(self.length):
            if(temp.value < x):
                LL1.append(temp.value)
                temp = temp.next
            else:
                LL2.append(temp.value)
                temp = temp.next
        temp1 = LL1.head
        while temp1.next is not None :
            temp1 = temp1.next
        temp1 = LL2.head
        for _ in range(LL2.length):
            while temp1 is not None:
                LL1.append(temp1.value)
                temp1 = temp1.next
        self.make_empty()
        temp2 = LL1.head
        for _ in range(LL1.length):
            self.append(temp2.value)
            temp2 = temp2.next

    
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

print(ll.partition_list(5))

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
