num = int(input("Enter a Number : "))
temp= num
reverse= 0
while temp > 0:
	digit = temp % 10
	reverse = reverse *10 + digit
	temp = temp // 10
if num == reverse:
	print("the number is a palindrome number")
else:
	print("The number is not a palindrome number")