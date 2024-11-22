from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# create dice
die_1 = Die(6)
die_2 = Die(6)

roll_results = []
frequencies = []

for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    roll_results.append(result)

max_result = die_1.num_sides * die_2.num_sides
for value in range (1, max_result+1):
    frequency = roll_results.count(value)
    frequencies.append(frequency)

# visualization
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
layout = Layout(title='Rolling two D6 1000 Times (Multiplied)', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': layout}, filename='d6_x_d6.html')