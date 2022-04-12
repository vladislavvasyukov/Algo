from data_structures.graphs.vertex import Vertex, VertexForBFS
from data_structures.queue import Queue


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, key):
        self.vertex_list[key] = Vertex(key)
        self.num_vertices += 1

    def get_vertex(self, n):
        return self.vertex_list.get(n)

    def __contains__(self, n):
        return n in self.vertex_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vertex_list:
            self.add_vertex(f)
        if t not in self.vertex_list:
            self.add_vertex(t)
        self.vertex_list[f].add_neighbor(self.vertex_list[t], cost)
        self.num_edges += 1

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def print_yourself(self):
        for vertex in self:
            for nbr in vertex.get_connections():
                print("( %s , %s )" % (vertex.get_id(), nbr.get_id()))


class GraphForBFS(Graph):
    def add_vertex(self, key):
        self.vertex_list[key] = VertexForBFS(key)
        self.num_vertices += 1

    @classmethod
    def build_graph(cls, word_file):
        d = {}
        g = cls()
        with open(word_file, 'r') as f:
            for line in f:
                word = line[:-1]

                for i in range(len(word)):
                    bucket = word[:i] + '_' + word[i + 1:]

                    if bucket in d:
                        d[bucket].append(word)
                    else:
                        d[bucket] = [word]

            for bucket in d.keys():
                for word1 in d[bucket]:
                    for word2 in d[bucket]:
                        if word1 != word2:
                            g.add_edge(word1, word2)
            return g

    @staticmethod
    def bfs(start):
        """
        :param start: instance VertexForBFS
        :return: None
        """
        start.distance = 0
        start.prev_vertex = None
        vertex_queue = Queue()
        vertex_queue.enqueue(start)
        while vertex_queue.size() > 0:
            current_vertex = vertex_queue.dequeue()
            for nbr in current_vertex.get_connections():
                if nbr.color == 'white':
                    nbr.color = 'gray'
                    nbr.distance = current_vertex.distance + 1
                    nbr.prev_vertex = current_vertex
                    vertex_queue.enqueue(nbr)
            current_vertex.color = 'black'

    def traverse(self, data):
        vertex = self.get_vertex(data)
        while vertex.prev_vertex:
            print(vertex.get_id())
            vertex = vertex.prev_vertex
        print(vertex.get_id())
