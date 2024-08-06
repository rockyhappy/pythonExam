import numpy as np

import matplotlib.pyplot as plt

food = np.array(["Meat","Banana","Avacados","Sweet Potato"])
Calories = np.array([250,130,140,120])
potasium = np.array([40,55,20,30])
fat = np.array([8,5,3,6])
print(food)
legend = ["Calories","Potasium","Fat"]
ypoints=[Calories,potasium,fat]
colors = ['red', 'blue', 'green']
plt.xlabel("Food")
plt.ylabel("Value")
plt.title("Food Value")

for i in range(3):
    plt.plot(food, ypoints[i], color=colors[i],label=legend[i])
    plt.legend()


plt.show()