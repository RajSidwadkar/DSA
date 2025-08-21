print("Enter total number of packets :")
n = int(input())
j=0
L=[0 for i in range (n)]
print("Enter number of chocolate in each packet :")
for i in range(n):
	a = int(input())
	if (a!=0):
		L[j] = a
		j+=1
for i in L:
	print( i, end = ' ')