class stack:
	stack_capacity = 8
	def __init__(self):
		self.data = [None]*stack.stack_capacity
		self.length = 0

	def is_empty(self):
		return self.length == 0

	def is_full(self):
		return self.data == stack.stack_capacity

	def stack_push(self,element):
		if not self.is_full():
			self.data.append(element)
		self.length += 1

	def stack_pull(self):
	 	if not self.is_empty():
	 		return self.data.pop()
	 		self.length -= 1

	def peak(self):
		if not self.is_empty():
			return self.data[-1]
	def show(self):
		return self.data

S=stack()
S.stack_push(10)
S.stack_push(12)
S.stack_push(13)
S.stack_push(15)
print S.show()