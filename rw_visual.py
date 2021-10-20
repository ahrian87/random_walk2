import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Making a random walk while the program stays active
while True:
    # Preparing random walk data
    rw = RandomWalk()
    rw.fill_walk()

    # Displaying random walk points
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == "n":
        break
