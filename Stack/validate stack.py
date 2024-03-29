class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack=[]
        i=0
        for num in pushed:
            stack.append(num) 
            while len(stack) >0 and stack[len(stack)-1] == popped[i] :
                stack.pop()
                i+=1 
        return True if len(stack) ==0 else False
    
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
obj = Solution()
print(obj.validateStackSequences(pushed, popped))