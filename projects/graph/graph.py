"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # creats a new node on the graph

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        v1_edges_set = self.vertices[v1] # connect to node one
        v1_edges_set.add(v2) # to node two

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue() # create an empty queue
        q.enqueue(starting_vertex) # enqueue the starting_vertex
        visited = set()  # create a set to track vertices we have visited
        while q.size() > 0: # while the queue isn't empty:
            current_node = q.dequeue() # dequeue, this is our current_node
            if current_node not in visited: # if we haven't visited it yet
                print(current_node)
                visited.add(current_node) # mark as visited
                neighbors = self.get_neighbors(current_node) # get its neighbors
                for neighbor in neighbors: # and add each to the back of queue
                    q.enqueue(neighbor)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        stack = Stack() # create an empty stack
        stack.push(starting_vertex) # push the starting_vertex onto the stack
        visited = set() # create a visited set
        while stack.size() > 0: # while our stack isn't empty:
            current_node = stack.pop() # pop off what's on top, this is our current_node
            if current_node not in visited: # if it hasn't been visited:
                print(current_node)
                visited.add(current_node) # mark it as visited
                neighbors = self.get_neighbors(current_node)  # get its neighbors
                for neighbor in neighbors: # and add each neighbor to the top of the stack
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # smae as above just with recursion

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)
        
        return visited


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue() # make a new queue
        visited = set() # make a visited node

        path = [starting_vertex] 

        q.enqueue(path) # qnqueue a PATH TO the starting node 

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]
            # if current_node not in visited:
            if current_node == destination_vertex:
                print("I'm here", current_path)
                return current_path

            if current_node not in visited:
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    path_copy = current_path[:]
                    current_path.append(neighbor)

                    q.enqueue(path_copy)

            # return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack() # initializing a stack

        path = [starting_vertex] # calling starting_vertex our path
    
        stack.push(path) # adding our starting vertex into the graph

        visited = set() # creating an already iterated node

        while stack.size() > 0: # while our stack isn't empty
            current_node = stack.pop() # pop off what's on top this is our current_node

            if current_node not in visited: # if 
                visited.add(current_node) # iterate through the node

                getPath = self.get_neighbors(current_node) # getting the path from starting_vertex to destination_vertex

                for path in getPath: # looping through our to find the path stack
                    return path # returning the path of the dfs

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = [starting_vertex]

        if path not in destination_vertex:
            destination_vertex.add(path)

            neighbors = self.get_neighbors(path)

            for neighbor in neighbors:
                self.dfs_recursive(neighbor, destination_vertex)

        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
