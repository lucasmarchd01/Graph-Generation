import random
import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.adj = {}

    def add_neighbours(self, neighbour, weight=0):
        """
        Add a neighbour to a vertex.

        :param neighbour: Neighbour node
        :param weight: weight of edge
        :return:
        """
        self.adj[neighbour] = weight

    def get_connections(self):
        """
        Get the neighbours of a vertex.

        :return:
        """
        return self.adj.keys()

    def get_weight(self, neighbour):
        """
        get the weight of the neighbours of a node.

        :param neighbour:
        :return:
        """
        return self.adj[neighbour]

    def __str__(self):
        return "{} neighbours: {}".format(self.key, [x.key for x in self.adj])


class Graph:

    def __init__(self, num_vertices=0, randomized=True, lower=10, higher=100):
        """
        Creates a graph by a randomiser or the ability to add and remove vertices/edges with specified weights.

        :param num_vertices: Number of vertices desired if creating graph randomly
        :param randomized: Boolean value representing if the graph should be randomized
        :param lower: Lower bound of the randomized graph edge weight values
        :param higher: Upper bond of the randomized graph edge weight values
        """
        self.vertices = {}
        self.num_vertices = 0
        if randomized:
            # Generate random graph
            for i in range(2, num_vertices + 1):
                x = random.randint(1, i - 1)
                S = random.sample(range(1, i), x)
                for s in S:
                    w = random.randint(lower, higher)
                    self.add_edge(i, s, w)

    def add_vertex(self, node):
        """
        Add a vertex to a graph.

        :param node: Node to add.
        :return:
        """

        # Create new vertex with Vertex class
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        self.num_vertices += 1

    def BFS(self):
        """
        Breadth-First Search traversal implementation of a graph. Randomly chooses a start vertex,
        and returns the total of the weights of the edges.

        :param v: Starting node
        :return: Total of the weights of the edges.
        """

        # Random start vertex
        v = random.choice(list(self.vertices))

        # Create list of visited vertices and set all to False
        visited = [False] * (self.num_vertices + 1)

        # Append start vertex to queue and set visited to True
        Q = []
        Q.append(v)
        visited[v] = True

        # Sum edge weights for all nodes.
        total = 0
        while Q:
            v = Q.pop(0)
            for nei in self.vertices[v].adj:
                if not visited[nei.key]:
                    Q.append(nei.key)
                    visited[nei.key] = True
                    total += self.vertices[v].get_weight(nei)
        return total

    def primMST(self):
        """
        Prim's algorithm to find the minimum spanning tree of a graph.

        :return: Total of the weights of the edges on the minimum spanning tree.
        """

        rand_num = random.randint(1, len(self.vertices) - 1)

        # pick a random vertex to start from
        start_v = self.vertices[rand_num]

        # total of the weights of the edges to be returned
        total = 0

        vertices = list(self.vertices.keys())
        visited = []

        # initialize k (vertex values/weights) and pi (parents)
        k = {}
        pi = {}

        # initialize k and pi with empty strings or very large numbers (infinity)
        for vertex in self.vertices:
            k[vertex] = ""
            pi[vertex] = sys.maxsize

        # alg for neighbours of the starting vertex.
        for nei in start_v.adj:
            # connect the vertices
            if pi[nei.key] == sys.maxsize or nei.get_weight(start_v) < pi[nei.key]:
                k[nei.key] = start_v.key
                pi[nei.key] = nei.get_weight(start_v)

        # update vertices and visited lists
        vertices.remove(rand_num)
        visited.append(rand_num)
        del k[rand_num]
        del pi[rand_num]

        # alg for the remaining vertices on the graph
        while vertices:
            min_weight = min(pi.items(), key=lambda x: x[1])

            # update the total weight with the minimum edge weight
            total += min_weight[-1]

            vertices.remove(min_weight[0])
            visited.append(min_weight[0])
            del k[min_weight[0]]
            del pi[min_weight[0]]

            # change the starting vertex
            start_v = self.vertices[min_weight[0]]

            # alg for neighbours of the starting vertex.
            for nei in start_v.adj:
                # see if the vertex has been visited
                if not (nei.key in visited):
                    # connect the vertices
                    if pi[nei.key] == sys.maxsize or nei.get_weight(start_v) < pi[nei.key]:
                        k[nei.key] = start_v.key
                        pi[nei.key] = nei.get_weight(start_v)
        return total

    def get_vertex(self, key):
        """
        Get a vertex from a graph.

        :param key: Vertex to find
        :return: Vertex. None if not found.
        """
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def __contains__(self, key):
        """
        Check if a vertex is present in the graph.

        :param key: Vertex to find.
        :return: True if found.
        """
        return key in self.vertices

    def add_edge(self, from_key, to_key, weight=0):
        """
        Add an edge to a graph between two vertices.

        :param from_key: Starting node.
        :param to_key: Ending node.
        :param weight: Weight between starting and ending node
        :return:
        """

        # Check if to and from vertices are already in the vertex list
        if from_key not in self.vertices:
            self.add_vertex(from_key)
        if to_key not in self.vertices:
            self.add_vertex(to_key)

        # Update the neighbour values for the to and from vertices.
        self.vertices[from_key].add_neighbours(self.vertices[to_key], weight)
        self.vertices[to_key].add_neighbours(self.vertices[from_key], weight)

    def get_vertices(self):
        """
        Get vertices from a graph

        :return: List of keys containing the vertices of the graph.
        """
        return self.vertices.keys()


def compare(k):
    """
    Function created to compare the Breadth-First search and the Pirm's minimum spanning tree algorithm
    for different values of n.

    :param k: Number of times to repeat the operation.
    :return:
    """

    # Sizes of graphs
    n_vals = [20, 40, 60]
    print("For input k of %d..." %k)
    for n in range(len(n_vals)):

        # Total of the differences for each k
        tot = 0
        for i in range(k):
            # generate graph and perform BFS/primMST
            g = Graph(n_vals[n])
            B = g.BFS()
            P = g.primMST()

            # Find diff and add to totals.
            diff = (B - P) / P * 100
            tot += diff
        avg = tot / k
        print("Average of values for diff for n=%d: %.2f%%" % (n_vals[n], avg))


if __name__ == "__main__":
    # Specify that the graph is not generated randomly and vertices/edged will be added manually.
    g2 = Graph(randomized=False)

    # Adding vertices and edges to graph
    g2.add_vertex(0)
    g2.add_vertex(1)
    g2.add_vertex(2)
    g2.add_vertex(3)
    g2.add_vertex(4)
    g2.add_vertex(5)
    g2.add_edge(0, 1, 15)
    g2.add_edge(0, 3, 7)
    g2.add_edge(1, 2, 9)
    g2.add_edge(1, 3, 11)
    g2.add_edge(0, 4, 10)
    g2.add_edge(2, 4, 12)
    g2.add_edge(3, 4, 8)
    g2.add_edge(1, 5, 9)
    g2.add_edge(2, 5, 7)
    g2.add_edge(3, 5, 14)
    g2.add_edge(4, 5, 8)

    print("\n------------Breadth First Search and Prim's Minimum Spanning Tree Comparison------------\n")
    # BFS
    print("Testing graph with Breadth-First Search algorithm: %d" % (g2.BFS()))

    # Prim's MST
    print("Testing graph with Prim's Minimum Spanning Tree algorithm: %d\n" % (g2.primMST()))

    # Compare BFS and MST with 10 repeats
    compare(10)
