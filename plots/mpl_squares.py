import matplotlib.pyplot as plt

# values
values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# set up
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

# generate plot
ax.plot(values, squares, linewidth=3)

# chart title and labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)
ax.tick_params(axis='both', labelsize=12)

plt.show()