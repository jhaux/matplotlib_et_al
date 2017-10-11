import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size=[1000])
f = plt.figure(figsize=(3, 2))

plt.hist(data)
plt.xlabel('value')
plt.ylabel('counts')

f.tight_layout()
plt.savefig('axis_labels.pgf')
plt.show()
