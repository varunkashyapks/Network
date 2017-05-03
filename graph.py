import sys
from queues import Array_queue

class Graph:
	# Inner class Vertex stores info about node
	# Vertex name, adjacent vertices stored in dict adjacent

	class Vertex:
		def __init__(self, node):
			self.vertex_id = node
			self.adjacent = {}

		#checks whether specified 'node' is already in dict adjacent
		def neighbour_present(self, node):	
			return node in self.adjacent

		# add neigbour node with cost
		def add_neighbour(self, neighbour, weight = 0):	
			if not self.neighbour_present(neighbour):
				self.adjacent[neighbour] = weight

		# return neighbouring nodes
		def get_neighbours(self):
			return self.adjacent.keys()

		# return vertex id
		def get_id(self):
			return self.vertex_id

		# return cost of specified neighbour, 
		# if node is not neighbour, return cost as infinite
		def get_weight(self, neighbour):
			if self.neighbour_present(neighbour):
				return self.adjacent[neighbour]
			else:
				return sys.maxsize

	def __init__(self):
		self.adjacency_list = {}
		self.graph_size = 0

	# Check whether graph is empty
	def is_empty(self):
		return self.graph_size == 0

	# return the number of nodes in graph
	def get_vertex_count(self):
		return self.graph_size


	# Add vertex to graph's adjacncy_list
	def add_vertex(self, node):
		if not node in self.adjacency_list:
			self.graph_size += 1
			new_vertex = self.Vertex(node)
			self.adjacency_list[node] = new_vertex

	# Redundent
	def get_vertex(self, node):
		if node in self.adjacency_list:
			return self.adjacency_list[node]
		else:
			return None

	# Add edge, passing start and end vertices with cost if any.
	# Assumes that graph is undirected. If want to have directed,
	# add edge only once.
	def add_edge(self, frm, to, weight = 0):
		if not frm in self.adjacency_list:
			self.add_vertex(frm)
		if not to in self.adjacency_list:
			self.add_vertex(to)
		self.adjacency_list[frm].add_neighbour(to, weight)
		self.adjacency_list[to].add_neighbour(frm, weight)

	# Returns all vertices of given graph
	def get_vertices(self):
		return self.adjacency_list.keys()

	# Returns list of adjacent nodes of given vertex
	def get_adjacent(self, vertex):
		if vertex in self.adjacency_list:
			neighbours = self.adjacency_list[vertex].get_neighbours()
			neighbours_list = []
			for v in neighbours:
				neighbours_list = neighbours_list + [v]
			return neighbours_list

	# return the edge cost of (frm, to)
	def get_edge_cost(self, frm, to):
		if frm  in self.adjacency_list and to in self.adjacency_list:
			cost = self.adjacency_list[frm].get_weight(to)
			return cost	


	# Returns sequence of verties from start node to end node, if path is present
	def find_path(self, start, end, path = []):
		path = path + [start]
		if start == end :
			return path
		if not start in self.adjacency_list:
			return None				
		neighbour_lst = self.get_adjacent(start)
		for node in neighbour_lst:
			if node not in path:
				new_path = self.find_path(node, end, path)
				if new_path : return new_path
		return None

	# Returns all availble paths between start and end vertices
	def find_all_paths(self, start, end, path = []):
		path = path + [start]
		if start == end:
			return [path]
		if not start in self.adjacency_list:
			return None
		paths = []

		neighbour_lst = self.get_adjacent(start)
		for node in neighbour_lst:
			if node not in path:
				new_paths = self.find_all_paths(node, end, path)
				for new_path in new_paths:
					paths.append(new_path)
		return paths

	# Dijkstras algorithm: Given source, returns shortest distances to all other nodes from source
	def shortest_path(self, start):
		visited = {}
		distance ={}
		neighbour_lst = self.adjacency_list.keys()

		for node in neighbour_lst:
			visited[node] = False
			distance[node] = self.adjacency_list[start].get_weight(node)
		visited[start] = True
		distance[start] = 0

		for node in neighbour_lst:
			vertex = self.choose_nearest_vertex(visited, distance)
			visited[vertex] = True
			for k in neighbour_lst:
				if not visited[k]:
					new_distance = distance[vertex] + self.adjacency_list[vertex].get_weight(k)
					if new_distance < distance[k] :
						distance[k] = new_distance
		return distance

	# return the nearest vertex from 'source' node to 
	# list of destination nodes (which are not yet discovered)
	def choose_nearest_vertex(self, visited, distance):
		neighbour_lst = self.adjacency_list.keys()
		minimum = sys.maxsize
		nearest = None
		for node in neighbour_lst:
			if distance[node] < minimum and not visited[node]:
				minimum = distance[node]
				nearest = node
		return nearest

	#Depth First Search
	def dfs(self, start):
		visited = {}
		self.__make_none(visited)
		self.__dfs(visited, start)

	# initialize visited[] of all nodes as None
	def __make_none(self, visited):
		neighbour_lst = self.adjacency_list.keys()
		for node in neighbour_lst:
			visited[node] = None

	# private method which implements dfs
	def __dfs(self, visited, start):
		visited[start] = True
		print (start)
		neighbour_lst = self.adjacency_list[start].get_neighbours()

		for vertex in neighbour_lst:
			if not visited[vertex]:
				self.__dfs(visited, vertex)


	# Breadth First Search
	def bfs(self, vertex):
		visited = {}
		self.__make_none(visited)
		q = Array_queue.ArrayQueue()
		visited[vertex] = True
		print(vertex)

		q.enqueue(vertex)
		while not q.is_empty():
			node = q.dequeue()
			neighbour_lst = self.adjacency_list[node].get_neighbours()
			for node in neighbour_lst:
				if not visited[node]:
					visited[node] = True
					print(node)
					q.enqueue(node)

