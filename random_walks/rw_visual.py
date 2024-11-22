import matplotlib.pyplot as plt
from random_walk import RandomWalk

# keep making more walks until user stops it
while True:
    # create RandomWalk object
    rw = RandomWalk(50_000)
    rw.fill_walk()
    
    # generate plot using RandomWalk object
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    # emphasize first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input('Go on another walk (y/n)? ')
    if keep_running == 'n':
        break