import math


from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, Range1d, LabelSet, Label, ColumnDataSource
from bokeh.palettes import Spectral8

from graph import *

canvas_width = 640
canvas_height = 480
CIRCLE_SIZE = 30

graph_data = Graph()
# graph_data.debug_create_test_data()
graph_data.randomize(5, 5, 10, 10)
graph_data.get_connected_components()
print(f"# of vertexes : {len(graph_data.vertexes)}")
for v in graph_data.vertexes:
    print(f"x : {v.pos['x']}    y: {v.pos['y']}")

N = len(graph_data.vertexes)
node_indices = list(range(N))

label_source = ColumnDataSource(data=dict(x=[vertex.pos['x'] for vertex in graph_data.vertexes], y=[
                                vertex.pos['y'] for vertex in graph_data.vertexes], value=[vertex.value for vertex in graph_data.vertexes]))
labels = LabelSet(x='x', y='y', text='value', level='glyph',
                  text_align='center', text_baseline='middle', source=label_source, render_mode='canvas')


color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(x_range=(0, canvas_width), y_range=(0, canvas_height),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color='color')

# this draws edges from start to end
start_nodes = []
end_nodes = []
count = 1
for vert in graph_data.vertexes:
    for edge in vert.edges:
        start_nodes.append(graph_data.vertexes.index(vert))
        end_nodes.append(graph_data.vertexes.index(edge.destination))


graph.edge_renderer.data_source.data = dict(
    start=start_nodes,
    end=end_nodes)

x = [vertex.pos['x'] for vertex in graph_data.vertexes]
y = [vertex.pos['y'] for vertex in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(labels)

output_file('graph.html')
show(plot)
