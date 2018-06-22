import random


class Edge:
    def __init__(self, destination):
        self.destination = destination
        self.weight = -1


class Vertex:
    def __init__(self, value, color, **pos):
        self.value = value
        self.edges = []
        self.pos = pos
        self.color = color

    def addEdge(self, edge):
        self.edges.append(edge)


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('v1', 'black', x=40, y=40)
        debug_vertex_2 = Vertex('v2', 'blue', x=80, y=80)
        debug_vertex_3 = Vertex('v3', 'yellow', x=400, y=243)
        debug_vertex_4 = Vertex('v4', 'green', x=480, y=125)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_edge_2 = Edge(debug_vertex_4)
        debug_edge_3 = Edge(debug_vertex_1)
        debug_edge_4 = Edge(debug_vertex_2)

        debug_vertex_1.edges.append(debug_edge_1)
        debug_vertex_2.addEdge(debug_edge_2)
        debug_vertex_3.addEdge(debug_edge_4)
        debug_vertex_4.addEdge(debug_edge_3)

        # print(f"edges : {debug_vertex_2.edges}")
        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])

    def bfs(self, start):
        random_color = "#" + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []
        found.append(start)
        queue.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                # TODO: add edge weight here
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0)
        return found

    def get_connected_components(self):
        searched = []
        for v in self.vertexes:
            if v not in searched:
                searched.append(self.bfs(v))

    def randomize(self, width, height, pxBox, probability):
        def connectVerts(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        count = 0
        grid = []

        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex('default', 'white', x=0, y=0)
                v.value = f"v{count}"
                count += 1
                row.append(v)
            grid.append(row)

        for y in range(height):
            for x in range(width):
                if (y < height - 1):
                    if random.randint(0, 50) < probability:
                        print(f"testing data       x: {x}  y: {y}")
                        connectVerts(grid[y][x], grid[y+1][x])
                if (x < width - 1):
                    if random.randint(0, 50) < probability:
                        connectVerts(grid[y][x], grid[y][x+1])

        boxBuffer = 0.8
        boxInner = pxBox * boxBuffer
        boxInnerOffset = (pxBox - boxInner) // 2

        for y in range(height):
            for x in range(width):
                grid[y][x].pos['x'] = int(
                    (x * pxBox + boxInnerOffset + (random.uniform(0, 50)) * boxInner))
                grid[y][x].pos['y'] = int(
                    (y * pxBox + boxInnerOffset + (random.uniform(0, 50)) * boxInner))

        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])
