import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

plt.style.use('classic')
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=3)

plt.show()