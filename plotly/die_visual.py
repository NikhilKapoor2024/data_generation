from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# create dice
die = Die()

roll_results = []
frequencies = []

for roll_num in range(1000):
    result = die.roll()
    roll_results.append(result)

for value in range (1, die.num_sides+1):
    frequency = roll_results.count(value)
    frequencies.append(frequency)

# visualization
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
layout = Layout(title='Rolling one D6 1000 Times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': layout}, filename='d6.html')