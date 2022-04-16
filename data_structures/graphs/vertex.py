class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return f'{self.id} connected to: {str([x.id for x in self.connected_to])}'


class VertexForBFS(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self._color = 'white'
        self._distance = 0
        self._prev_vertex = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def prev_vertex(self):
        return self._prev_vertex

    @prev_vertex.setter
    def prev_vertex(self, value):
        self._prev_vertex = value
