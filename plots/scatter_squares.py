import matplotlib.pyplot as plt

# x and y values
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# generate scatter
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# chart title and labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.axis([0, 1100, 0, 1_100_000])

plt.show()