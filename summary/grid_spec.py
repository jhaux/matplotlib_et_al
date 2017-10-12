import matplotlib.pyplot as plt
import matplotlib.gridspec as GS
import numpy as np
import matplotlib as mpl

latex_preamble = {
    "font.family": "serif",        # use serif/main font for text elements
    "text.usetex": True,           # use inline math for ticks
    "text.latex.preamble": [
        r"\usepackage{amsmath}",   # for the align environment
        ]
    }

mpl.rcParams.update(latex_preamble)

a, o = -10*np.pi, 10*np.pi
X = np.linspace(a, o, num=300)
Y = np.exp(-X/10) * np.sin(X)
Z = 10 + np.exp(-X/10) * np.cos(X)

f = plt.figure(figsize=(5, 3))  # Create figure expilcitly $\label{li:fig}$

gs = GS.GridSpec(2, 2,
        width_ratios=[1, 0.5])  # left ax half as wide as right ax $\label{li:gswr}$
ax1 = f.add_subplot(gs[0,0])  # Explicit handles for each axes $\label{li:ax}$
ax2 = f.add_subplot(gs[0,1])
ax3 = f.add_subplot(gs[1,:])  # axes spanning the whole row $\label{li:gsslice}$

ax1.hist(Y, ec='k', alpha=0.5, label='Y')  # Plot a translucent Histogram $\label{li:hist}$
ax1.hist(Z, ec='k', alpha=0.5, label='Z')
ax1.legend()  # Make a legend using the labels supplied above $\label{li:leg}$
ax1.set_xlabel('Value')
ax1.set_ylabel('Counts')

ax2.plot(Y, Z)  # Make a line plot $\label{li:plot}$
ax2.set_aspect(1)
ax2.set_xlabel('Y')
ax2.set_ylabel('Z')

ax3.plot(X, Y)
ax3.plot(X, Z)
ax3.annotate(r'$10 + e^{-\frac{x}{10}} \cdot \cos{x}$',  # Write LaTeX $\label{li:ann}$
             xy=[X[90], Z[90]], xytext=[0.9, 0.9],
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3,rad=0.2'),
             textcoords='axes fraction',
             va='top', ha='right',
             fontsize=12)
ax3.axhline(Y.mean(), c='k', ls='--', lw=0.5) # Draw a dashed line $\label{li:hl}$
Y_slice = Y[:90]
print(Y_slice.max())
print(Y_slice.min())
start = X[:90][Y_slice==Y_slice.max()]
stop = X[:90][Y_slice==Y_slice.min()]
stop += stop - start
print(start)
print(stop)
ax3.axvspan(start, stop, alpha=0.2)  # Draw a translicent area $\label{li:vs}$
ax3.set_xlabel('X')
ax3.set_ylabel('Y, Z')

ax1.yaxis.set_label_coords(-0.2, 0.5)  # Move the label $\label{li:lbc}$
ax3.yaxis.set_label_coords(-0.1, 0.5)

f.tight_layout()
f.savefig(__file__.replace('py', 'pgf'))
plt.show()
