class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n 
        stack = []  

        # First Iteration
        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = nums[i % n]  

            stack.append(i % n) 

        # Second Iteration
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                # Pop elements from stack while nums[i] is greater than the top element
                popped_index = stack.pop()
                result[popped_index] = nums[i]  # Set the next greater element for the popped element

        return result