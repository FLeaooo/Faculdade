import math
import matplotlib.pyplot as plt

# Create a list L0 containing numbers in sequence from 0 to 100
L0 = list(range(101))

# Create a list L1 with the square of each element in L0
L1_square = [x**2 for x in L0]

# Create a list L2 with the sine of each element in L0
L2_sine = [math.sin(math.radians(x)) for x in L0]

# Create a list L3 with the cosine of each element in L0
L3_cosine = [math.cos(math.radians(x)) for x in L0]

# Create a figure and three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

# Plot the square function
ax1.plot(L0, L1_square, label='Square')
ax1.set_ylabel('Square')
ax1.legend()

# Plot the sine function
ax2.plot(L0, L2_sine, label='Sine')
ax2.set_ylabel('Sine')
ax2.legend()

# Plot the cosine function
ax3.plot(L0, L3_cosine, label='Cosine')
ax3.set_xlabel('L0')
ax3.set_ylabel('Cosine')
ax3.legend()

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
