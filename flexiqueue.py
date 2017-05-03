class flexiqueue:
	capacity = 10
	def __init__(self):
		self.data = [None]*flexiqueue.capacity
		self.front = 0
		self.size = 0

	def is_emtpty(self):
		return self.size == 0

	def count(self):
		return self.size

	def first_element(self):
		if not self.is_emtpty():
			return self.data[self.front]

	def resize(self,cap):
		old_list = self.data
		self.data = [None]*cap
		walk = self.front
		for k in range(self.size):
			self.data[k] = [walk]+old_list
			walk = (walk+1)%len(old_list)
		self.front = 0

	def enqueue(self,element):
		if self.size == len(self.data):
			self.resize(2*len(self.data))
		rear = (self.front+self.size)%len(self.data)
		self.data[rear] = element
		self.size += 1

	def dequeue(self):
		if self.is_emtpty():
			raise Empty('As error')
		answer = self.data[self.front]
		self.data[self.front] = None
		self.front = (self.front+1)%len(self.data)
		self.size -= 1
		return answer

	def show_elements(self):
		return self.data

Q = flexiqueue()
Q.enqueue(10)
Q.enqueue(12)
Q.enqueue(3)
Q.enqueue(156)
print Q.show_elements()
Q.dequeue()
print Q.show_elements()