import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Creating a figure and a set of subplots
fig, ax = plt.subplots(figsize=(8, 8))

# Defining various patches for the circuit elements
Vdd = mpatches.Circle((2, 4), 0.1, color='blue', ec='black')
I1 = mpatches.Rectangle((1.5, 2), 0.2, 1, edgecolor='black', facecolor='none')
Vgate = mpatches.Circle((0.5, 2), 0.1, color='blue', ec='black')
R = mpatches.Rectangle((0.7, 3), 0.2, 1, edgecolor='black', facecolor='none')
NMOS1 = mpatches.Rectangle((1.7, 3), 0.6, 1, edgecolor='black', facecolor='none')
NMOS2 = mpatches.Rectangle((2.7, 3), 0.6, 1, edgecolor='black', facecolor='none')

# Adding patches to the axes
ax.add_patch(Vdd)
ax.add_patch(I1)
ax.add_patch(Vgate)
ax.add_patch(R)
ax.add_patch(NMOS1)
ax.add_patch(NMOS2)

# Drawing the circuit
plt.plot([2, 2], [3.5, 4.3], color='black')  # Line from Vdd to NMOS2
plt.plot([2, 1.5], [2, 2], color='black')  # Line from I1 to NMOS2
plt.plot([1.7, 1.7], [3, 2], color='black')  # Line from NMOS1 to I1
plt.plot([1.7, 1.7], [4, 4.5], color='black')  # Line from NMOS1 to top
plt.plot([2.7, 2.7], [4, 4.5], color='black')  # Line from NMOS2 to top
plt.plot([3.3, 3.3], [4, 4.5], color='black')  # Line from NMOS2 source to top
plt.plot([0.7, 0.7], [3, 2], color='black')  # Line from Resistor to I1
plt.plot([0.7, 1.7], [3, 3], color='black')  # Line from Resistor to NMOS1
plt.plot([0.5, 0.7], [2, 2], color='black')  # Line from Vgate to I1
plt.plot([0.5, 0.5], [2, 1.5], color='black')  # Line from Vgate to bottom
plt.plot([1.7, 1.7], [3, 1.5], color='black')  # Line from NMOS1 to bottom

# Adding text/annotations to the plot
plt.text(2, 4.3, '$V_{dd}$', fontsize=12, verticalalignment='bottom', horizontalalignment='center')
plt.text(0.5, 1.5, '$V_{gate}$', fontsize=12, verticalalignment='top', horizontalalignment='center')
plt.text(1.7, 3.7, '$M_1$', fontsize=12, verticalalignment='center', horizontalalignment='center')
plt.text(2.7, 3.7, '$M_2$', fontsize=12, verticalalignment='center', horizontalalignment='center')
plt.text(1.5, 2.5, '$I_1$', fontsize=12, verticalalignment='center', horizontalalignment='center')
plt.text(0.7, 3.5, 'R', fontsize=12, verticalalignment='center', horizontalalignment='center')

# Adding ground symbol
plt.plot([3.3, 3.3], [1.5, 1], color='black')  # Line from NMOS2 source to ground
plt.plot([3.1, 3.3, 3.5], [1, 1.2, 1], color='black')  # Ground symbol

# Adjusting the plot limits and turning off the axes
plt.xlim(-1, 5)
plt.ylim(0, 5)
plt.axis('off')
plt.show()