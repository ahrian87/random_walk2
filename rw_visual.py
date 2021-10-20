import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Making a random walk while the program stays active
while True:
    # Preparing random walk data
    rw = RandomWalk()
    rw.fill_walk()

    # Displaying random walk points
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=15)
    # Showing starting and ending point with different colors
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Hiding the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == "n":
        break
