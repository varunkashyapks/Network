class l_list:
	class Node:
		def _init__(self,info):
			self.data = []
			self.next = None


	def _init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def is_empty(self):
		return self.length == 0

	def add_at_head(self,element):
		node = self.Node(element)
		if self.is_empty():
			node.next = self.head
			self.head.node
		else:
			self.head = self.tail = node
		self.length += 1

	def add_at_tail(self,element):
		new = self.Node(element)
		if not self.is_empty():
			new.next = None
			self.tail.next = new
			self.tail.new
		else:
			self.head = self.tail = new
		self.length += 1

	def delete_at_head(self):
		if not self.is_empty():
			data = self.head.data
			self.head = self.head.next
		self.length -= 1

L = l_list()		
L.add_at_head(110)

