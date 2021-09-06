from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
#ax = fig.axes(fig)
ax = plt.axes(projection='3d')

B_davinci = [14.33333333, 12.33333333, 6, 12, 4.333333333]
N_davinci = [5.333333333, 5.666666667, 9.666666667, 9.333333333, 8.333333333]
S_davinci = [4.666666667, 6.333333333, 8.666666667, 3, 11.66666667]
tot_davinci = [49, 38.33333333, 34.33333333]

B_curie = [4.666666667, 4, 6, 2.666666667, 4]
N_curie = [4.333333333, 9.333333333, 6, 5.666666667, 11.33333333]
S_curie = [15.33333333, 11, 12.33333333, 16, 9]
tot_curie = [21.33333333, 36.66666667, 63.66666667]

B_human = [5.333333333, 8, 12.33333333, 9.666666667, 16]
N_human = [14.66666667, 9.333333333, 8.666666667, 9.333333333, 4.666666667]
S_human = [4.333333333, 7, 3.333333333, 5.333333333, 3.666666667]
tot_human = [51.33333333, 46.66666667, 23.66666667]

davinci = ax.scatter3D(N_davinci, S_davinci, B_davinci, marker='o')
curie = ax.scatter3D(N_curie, S_curie, B_curie, marker='^')
human = ax.scatter3D(N_human, S_human, B_human, marker='+')

ax.set_zlabel('Best')
ax.set_xlabel('Next Best')
ax.set_ylabel('Worst')
ax.legend((davinci, curie, human),
            ('Davinci','Curie','Human'))

plt.show()