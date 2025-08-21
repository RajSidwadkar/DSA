n = int(input("Enter total number of choc packets :"))
L = [0 for i in range(n)]
j = 0
print("Enter number of chocolates in each packet :")
for i in range(n):
	a = int(input())
	if(a!=0):
		L[j] = a
		j += 1
for i in  L:
	print(i, end = '') 
		