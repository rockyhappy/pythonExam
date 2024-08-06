import numpy as np

import matplotlib.pyplot as plt

players = np.array(['Virat', 'Rohit', 'Shikhar', 'Hardik'])
runs1 = [51, 87, 45, 67]
runs2 = [67, 89, 78, 45]
runs3 = [55, 78, 78, 67]

x = np.arange(len(players))
width = 0.2
colors = ['red', 'green', 'blue']
print(x)
plt.bar(x - width, runs1, width=width, color=colors[0], label='Match 1',)
plt.bar(x, runs2, width=width, color=colors[1], label='Match 2', )
plt.bar(x + width, runs3, width=width, color=colors[2], label='Match 3')

plt.xlabel('Players')
plt.ylabel('Runs')
plt.title('Runs Scored by Players')

plt.xticks(x, players)  # Set player names as x-axis labels

plt.legend()
plt.show()
