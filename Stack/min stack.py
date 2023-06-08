class MinStack(object):

    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)
        

    def pop(self):
        self.stack_list.pop()
        

    def top(self):
        return self.stack_list[-1]
        

    def getMin(self):
        min = float('inf')
        for i in range(len(self.stack_list)-1, -1, -1):
            if min > self.stack_list[i]:
                min = self.stack_list[i]
        return min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())