import matplotlib.pyplot as plt
import numpy as np

players = np.array([1,3,5,7])
players2 = np.array([2,4,6,8])
runs1 = [51, 87, 45, 67]
runs2 = [67, 89, 78, 45]
plt.bar(players,runs1, color='green', label="gth")
plt.bar(players2,runs2, color='red', label="ght")
plt.legend()
plt.xlabel('Players')
plt.ylabel('Runs')
plt.title('Runs Scored by Players')
plt.show()