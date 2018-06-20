class Edge:
    def __init__(self, destination):
        self.destination = destination
        self.weight = -1


class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.edges = []
        self.pos = pos
        self.color = 'white'

    def addEdge(self, edge):
        self.edges.append(edge)


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('P1', x=40, y=40)
        debug_vertex_2 = Vertex('P2', x=80, y=80)
        debug_vertex_3 = Vertex('P3', x=400, y=243)
        debug_vertex_4 = Vertex('P4', x=480, y=125)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)
        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])
