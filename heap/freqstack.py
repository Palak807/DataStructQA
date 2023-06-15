class FreqStack(object):

    def __init__(self):
        self.stack_list = []
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
        

    def push(self, val):
        self.stack_list.append(val)
        

    def pop(self):

        maxCount = 0

        mapper = {}
        for k in range(len(self.stack_list)-1, -1, -1):
            i = self.stack_list[k]
            mapper[i] = mapper.get(i, 0) + 1

        for value, count in mapper.items():
            maxCount = max(maxCount, count)
        # print(maxCount)

        for value, count in mapper.items():
            if count == maxCount:
                self.stack_list.remove(value)
                return value

        # print(mapper)
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(9)
obj.push(8)
obj.push(8)
obj.push(8)
obj.push(9)
obj.push(9)
# obj.print_stack()
obj.pop()
obj.print_stack()
# param_2 = obj.pop()