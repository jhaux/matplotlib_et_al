import matplotlib.pyplot as plt
import numpy as np

a, o = -10*np.pi, 10*np.pi
X = np.linspace(a, o, num=300)
Y = np.exp(-X/10) * np.sin(X)

datum = X[200], Y[200]

f, ax = plt.subplots(figsize=(3,3))

ax.plot(X, Y)
ax.text(0.9, 0.9, 'Well, hello there!',
        verticalalignment='top',
        horizontalalignment='right',
        transform=ax.transAxes)

ax.annotate('important!',
        xy=datum,
        xytext=(0.5, 0.2),
        textcoords=ax.transAxes,
        arrowprops=dict(arrowstyle='->',
            connectionstyle='arc3,rad=0.3',
            facecolor='black',
            shrinkB=10))

f.tight_layout()
f.savefig(__file__.replace('py', 'pgf'))
plt.show()
