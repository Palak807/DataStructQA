def generatePrintBinary(n):

	from queue import Queue
	q = Queue()
	q.put("1")

	while(n > 0):
		n -= 1
		s1 = q.get()
		print(s1)

		s2 = s1 # Store s1 before changing it

		q.put(s1+"0")

		q.put(s2+"1")


if __name__ == "__main__":
	n = 10

	generatePrintBinary(n)
