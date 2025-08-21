def printNums(n):
	if n == 0:
		return
	print(n)
	printNums(n-1)
n = int(input("Enter any Number :\n"))
printNums(n)