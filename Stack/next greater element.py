class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def NGE(arr):
    s = Stack()
    element = 0
    next = 0

    s.push(arr[0])

    for i in range(1, len(arr), 1):
        next = arr[i]
        if s.is_empty() == False:
            element = s.pop()

            while(element < next):
                print(str(element) + " ---> " + str(next))
                if s.is_empty() == True:
                    break
                element = s.pop()

            if element > next:
                s.push(element)
        
        s.push(next)

    while s.is_empty() == False:
        element = s.pop()
        next = -1
        print(str(element) + " ---> " + str(next))

arr = [11, 13, 21, 3]
NGE(arr)