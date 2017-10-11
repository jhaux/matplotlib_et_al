import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size=[1000])

plt.hist(data)

plt.savefig(__file__.replace('py', 'png'))
plt.show()
