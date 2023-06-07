#User function Template for python3
class Solution:
    def bracketNumbers(self, S):
        stack = []
        opening_brackets = ["(", "[", "{"]
        closing_brackets = [")", "]", "}"]

        count = 0
        ans = []

        for char in S:
            if char in opening_brackets:
                count += 1
                stack.append(count)
                ans.append(count)
            elif char in closing_brackets:
                ans.append(stack.pop())

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.bracketNumbers(S)
		for value in answer:
			print(value, end = " ")
		print()


# } Driver Code Ends