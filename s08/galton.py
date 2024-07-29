import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters
num_balls = 100  # Number of balls
num_levels = 10  # Number of levels in the Galton board

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, num_levels + 1)
ax.set_ylim(-1, num_levels + 1)
ax.set_xticks([])
ax.set_yticks([])

# Create bins
bins = np.zeros(num_levels + 1)
bin_centers = np.arange(num_levels + 1)

# Create scatter plot for balls
balls = np.zeros((num_balls, 2))
scat = ax.scatter([], [], s=10)

def init():
    """Initialize the animation."""
    scat.set_offsets([])
    return scat,

def update(frame):
    """Update the animation by moving one ball at a time."""
    global balls, bins

    for ball in balls:
        if ball[1] < num_levels:
            direction = np.random.choice([-1, 1])
            ball[0] += direction * 0.5
            ball[1] += 1

    # Clear the axis
    ax.clear()

    # Update bin counts
    for ball in balls:
        if ball[1] == num_levels:
            bins[int(ball[0] + num_levels // 2)] += 1

    # Plot the balls
    scat.set_offsets(balls)

    # Plot the bins
    ax.bar(bin_centers, bins, width=0.9, color='gray', alpha=0.5, align='center')

    # Plot settings
    ax.set_xlim(-1, num_levels + 1)
    ax.set_ylim(-1, num_levels + 1)
    ax.set_xticks([])
    ax.set_yticks([])

    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_balls, init_func=init, blit=True, interval=100, repeat=False)

plt.show()