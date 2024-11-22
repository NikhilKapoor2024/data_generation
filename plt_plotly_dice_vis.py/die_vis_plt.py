import matplotlib.pyplot as plt
from die import Die

die = Die()
roll_results = []
frequencies = []

for roll_num in range(1000):
    result = die.roll()
    roll_results.append(result)

for value in range (1, die.num_sides+1):
    frequency = roll_results.count(value)
    frequencies.append(frequency)

values = [1, 2, 3, 4, 5, 6]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

ax.plot(values, frequencies, linewidth=3)

ax.set_title("Rolling a D6 1000 Times", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Frequency Rolled", fontsize=12)
ax.tick_params(axis='both', labelsize=12)

plt.show()