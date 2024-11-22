from plotly.graph_objs import Bar, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk(3)
rw.fill_walk()

x_values = list(range((-1*rw.num_points), rw.num_points))
y_values = list(range((-1*rw.num_points), rw.num_points))
data = [Bar(x=x_values, y=y_values)]
x_config = {"title": 'Random Walk', 'dtick': 1}
y_config = {'title': 'Straight up random as heck'}
layout = Layout(title='Random Walk', xaxis=x_config, yaxis=y_config)
offline.plot({'data': data, 'layout': layout}, filename='rw.html')
