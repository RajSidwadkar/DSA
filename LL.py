class Node:
	def __first__(self, data):
		self.data = data
		self.next = None
n1 = Node(7)
print(n1.data)
print(n1.next)