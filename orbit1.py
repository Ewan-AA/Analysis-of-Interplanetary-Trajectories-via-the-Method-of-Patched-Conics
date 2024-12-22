import numpy as np
import matplotlib.pyplot as plt

# Arbitrary constants
# Mass of spacecraft (arbitrary units), cancels out in energy
L = 1.2        # Angular momentum (arbitrary units)
r_min = .5      # Minimum radius (arbitrary units)
r_max = 20.0     # Maximum radius (arbitrary units)

# Radial distances (avoid division by zero)
r = np.linspace(r_min, r_max, 200)

# Effective potential function (arbitrary units)
U_eff = L**2/(2*r**2)-1/r

# Plot the effective potential
plt.figure(figsize=(8, 6))
plt.plot(r, U_eff, label=r'$U_{\text{eff}}(r) = \frac{L^2}{2mr^2} - G\frac{Mm}{r}$')
plt.axhline(y=-0.15, color='red', linestyle='--', label='Total Energy')
# Add labels and title
plt.xlabel('Radius (r) [arbitrary units]')
plt.ylabel('Effective Potential $U_{\text{eff}}(r)$ [arbitrary units]')
plt.title('Effective Potential vs. Radius')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
