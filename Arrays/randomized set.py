import random

class RandomizedSet(object):
    def __init__(self):
        self.index = {}
        self.arr = []

    def insert(self, val):
        if val not in self.arr:
            self.arr.append(val)
            self.index[val] = True
            return True
        return False

    def remove(self, val):
        if val in self.arr:
            self.arr.remove(val)
            del self.index[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.arr)
 


obj = RandomizedSet()
param_1 = obj.insert(5)
param_2 = obj.insert(6)
param_3 = obj.insert(7)
param_4 = obj.insert(8)
param_5 = obj.insert(9)
param_5 = obj.remove(9)
param_5 = obj.insert(9)
print(obj.index, obj.arr)
print(obj.getRandom())