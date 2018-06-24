#15816052
#滝浦良木

import numpy as np
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


fig, ax = plt.subplots()

ax.plot(np.arange(1, 13, 1), np.random.uniform(30, 80, 12), '-o', ms=5, lw=1, alpha=0.7, mfc='blue')
ax.grid()

plt.xlim(1, 12)
plt.ylim(30, 80)
plt.xlabel('Month')
plt.ylabel('Money [10000yen]')
plt.title('Earned money per month in 2017')
plt.minorticks_on()
plt.show()
