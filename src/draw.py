import math


from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Range1d, LabelSet, Label, ColumnDataSource
from bokeh.palettes import Spectral8

from graph import *

canvas_width = 500
canvas_height = 500

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

label_source = ColumnDataSource(data=dict(x=[vertex.pos['x'] for vertex in graph_data.vertexes], y=[
                                vertex.pos['y'] for vertex in graph_data.vertexes], value=[vertex.value for vertex in graph_data.vertexes]))
labels = LabelSet(x='x', y='y', text='value', level='glyph',
                  x_offset=-10, y_offset=-10, source=label_source, render_mode='canvas')

# debug_pallete = Spectral8
# debug_pallete.append('#ff0000')
# debug_pallete.append('#0000ff')

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0, canvas_width), y_range=(0, canvas_height),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=20, width=30, fill_color='color')

# this draws edges from start to end
start_nodes = []
end_nodes = []
count = 1
for vert in graph_data.vertexes:
    # if len(vert.edges) > 0:
    for edge in vert.edges:
        start_nodes.append(graph_data.vertexes.index(vert))
        end_nodes.append(graph_data.vertexes.index(edge.destination))

        # for v in graph_data.vertexes:
        #     if v.value == edge.value:
        print(f"start : {start_nodes}")
        print(f"end   : {end_nodes}")

graph.edge_renderer.data_source.data = dict(
    start=start_nodes,
    end=end_nodes)
# print(f"start : {[0]*N}")
# print(f"end   : {node_indices}")
# start of layout code

x = [vertex.pos['x'] for vertex in graph_data.vertexes]
y = [vertex.pos['y'] for vertex in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(labels)

output_file('graph.html')
show(plot)
