import matplotlib.pyplot as plt

# x and y values
x_values = range(5000)
y_values = [x**3 for x in x_values]

# generating plot
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, linewidth=3, c=y_values, cmap=plt.cm.viridis)

# custom titles and labels
ax.set_title('Cubed Numbers', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubes of Values', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()


