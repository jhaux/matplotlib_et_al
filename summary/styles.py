import matplotlib.pyplot as plt
import numpy as np

a, o = -10*np.pi, 10*np.pi
X = np.linspace(a, o, num=300)
Y = np.exp(-X/10) * np.sin(X)
Z = np.exp(-X/10) * np.cos(X)

f, (ax1, ax2) = plt.subplots(2, 1, figsize=(3,5))

with plt.style.context('seaborn'):
    ax1.plot(X, Y)
    ax1.plot(X, Z)

ax2.plot(X, Y)
ax2.plot(X, Z)

f.tight_layout()

f.savefig(__file__.replace('py', 'pgf'))
plt.show()
