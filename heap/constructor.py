class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp

            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        
        if len(self.heap) == 2:
            return self.heap.pop()

        ans = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1

        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and
                self.heap[i] > self.heap[i * 2 + 1]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp

                i = i * 2 + 1

            elif self.heap[i] > self.heap[(i * 2)] :
                tmp = self.heap[i]
                self.heap[i] = self.heap[(i * 2)] 
                self.heap[(i * 2)]  = tmp

                i = i * 2
            
            else:
                break 

        return ans
    
    def heapify(self, arr):
        arr.append([arr[0]])

        self.heap = arr
        cur = (len(self.heap) - 1 )//2

        while cur > 0 :
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                    self.heap[2 * i + 1] < self.heap[2 * i] and
                    self.heap[i] > self.heap[i * 2 + 1]):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i * 2 + 1]
                    self.heap[i * 2 + 1] = tmp

                    i = i * 2 + 1

                elif self.heap[i] > self.heap[(i * 2)] :
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[(i * 2)] 
                    self.heap[(i * 2)]  = tmp

                    i = i * 2
                
                else:
                    break 

        cur -= 1 





    def print(self):
        ans = []
        for i in self.heap:
            ans.append(i)
        return ans

my_heap = Heap()
my_heap.push(9)
my_heap.push(18)
my_heap.pop()
print(my_heap.print())
