import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Maximum and minimum sensor values: x,y
max_x = 255
min_x = -255
max_y = 255
min_y = -255

# Lower and upperbounds of the ideal operating zones
happy_x_lower = 50
happy_x_upper = 200
happy_y_lower = 50
happy_y_upper = 200

inner_circle = plt.Circle(((max_x + min_x) / 2, (max_y + min_y) / 2), happy_x_lower, color='r', clip_on=False)
green_zone = plt.Circle(((max_x + min_x) / 2, (max_y + min_y) / 2), happy_x_upper, color='w', clip_on=False)
outer_circle = plt.Circle(((max_x + min_x) / 2, (max_y + min_y) / 2), max_x, color='r', clip_on=False)


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read x,y sensor inputs, can also be passed in if needed, specify in fargs of FuncAnimation
    xaxis_input = random.randint(min_x, max_x)
    yaxis_input = random.randint(min_y, max_y)

    # Add inputs to axes
    xs.append(xaxis_input)
    ys.append(yaxis_input)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    
    # Draw operating zones
    ax.add_patch(outer_circle)
    ax.add_patch(green_zone)
    ax.add_patch(inner_circle)
    ax.plot(xs, ys)
    
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Sensor Inputs')
    plt.ylabel('Y-value')
    plt.xlabel('X-value')
    print("Coordinates X:{} Y:{}".format(xaxis_input, yaxis_input))

# Set up plot to call animate() function every 100ms
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()
