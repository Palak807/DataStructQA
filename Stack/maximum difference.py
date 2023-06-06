def left(arr, n, SE):

	stack = []
	for i in range(n):
		
		while(stack != [] and stack[len(stack)-1] >= arr[i]):
			stack.pop()

		if(stack != []):
			SE[i]=stack[len(stack)-1]
		else:
			SE[i]
		stack.append(arr[i])

def findMaxDiff(arr, n):
	ls=[0]*n 
	rs=[0]*n 

	left(arr, n, ls)
	
	left(arr[::-1], n, rs)
	res = -1
	for i in range(n):
		res = max(res, abs(ls[i] - rs[n-1-i]))
	return res

	
if __name__=='__main__':
	arr = [2, 4, 8, 7, 7, 9, 3]
	print ("Maximum Diff :", findMaxDiff(arr, len(arr)))
	
