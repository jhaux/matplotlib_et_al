import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def plot_matrix(ax, values, norm=None):
    x_max, y_max = values.shape

    if norm is None:
        plot_values = values / np.abs(values).max()
    else:
        plot_values = values / norm

    for x in range(x_max):
        for y in range(y_max):
            z = plot_values[x,y]
            size = np.abs(z)
            color = 'w' if np.sign(z) > 0 else 'k'
            rect = patches.Rectangle((x-size/2., y-size/2.), size, size, fc=color)
            ax.add_patch(rect)
            ax.set_xlim(-1, x_max)
            ax.set_ylim(-1, y_max)
            ax.set_aspect(1)
            ax.set_facecolor('gray')

A = np.random.uniform(-1, 1, size=[10, 10])

f, ax = plt.subplots(figsize=(3,3))
plot_matrix(ax, A)

f.savefig(__file__.replace('py', 'pgf'))
plt.show()
